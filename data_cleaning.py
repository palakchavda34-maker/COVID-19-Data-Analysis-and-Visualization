"""Load, inspect, and clean the Kaggle Novel Coronavirus 2019 dataset."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
OUTPUT_DIR = DATA_DIR / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def find_dataset():
    candidates = [
        DATA_DIR / "covid_19_data.csv",
        DATA_DIR / "COVID-19.csv",
        DATA_DIR / "covid19.csv",
    ]
    for path in candidates:
        if path.exists():
            return path
    csv_files = [p for p in DATA_DIR.glob("*.csv") if "cleaned" not in p.name.lower()]
    if csv_files:
        return csv_files[0]
    raise FileNotFoundError(
        "Dataset CSV not found. Download the Kaggle dataset and place its CSV file "
        "inside the project's data/ folder. The common filename is covid_19_data.csv."
    )

def clean_data():
    source = find_dataset()
    df = pd.read_csv(source)
    print(f"Loaded: {source.name}")
    print(f"Original shape: {df.shape}")
    print("\nOriginal missing values:\n", df.isna().sum())
    print("\nOriginal data types:\n", df.dtypes)

    # Standardize common column names without assuming every dataset version is identical.
    rename = {
        "ObservationDate": "ObservationDate",
        "Country/Region": "Country_Region",
        "Country/Region ": "Country_Region",
        "Province/State": "Province_State",
        "Last Update": "Last_Update",
    }
    df = df.rename(columns=rename)

    required = ["ObservationDate", "Confirmed", "Deaths", "Recovered"]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Required columns not found: {missing}. Available columns: {list(df.columns)}")

    if "Country_Region" not in df.columns:
        raise ValueError("Could not find the country column (expected Country/Region).")

    # Remove only exact duplicate rows; similar rows can represent separate locations.
    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()
    print(f"\nExact duplicate rows removed: {duplicate_count}")

    df["ObservationDate"] = pd.to_datetime(df["ObservationDate"], errors="coerce")
    invalid_dates = int(df["ObservationDate"].isna().sum())
    df = df.dropna(subset=["ObservationDate"]).copy()
    print(f"Rows removed due to invalid/missing dates: {invalid_dates}")

    df["Country_Region"] = df["Country_Region"].fillna("Unknown").astype(str).str.strip()
    if "Province_State" in df.columns:
        df["Province_State"] = df["Province_State"].fillna("Unknown").astype(str).str.strip()

    numeric_cols = ["Confirmed", "Deaths", "Recovered"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        missing_before = int(df[col].isna().sum())
        # Missing case counts are filled with zero and documented; this is a pragmatic
        # preprocessing choice, not a claim that missing values were truly zero.
        df[col] = df[col].fillna(0)
        df[col] = df[col].clip(lower=0)
        print(f"{col}: {missing_before} missing/non-numeric values filled with 0; negatives clipped to 0.")

    # Flag potential outliers using the IQR rule. Do not automatically delete them:
    # large counts can be legitimate in a real-world epidemiological dataset.
    outlier_report = []
    for col in numeric_cols:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        count = int(((df[col] < lower) | (df[col] > upper)).sum())
        outlier_report.append({
            "column": col, "q1": q1, "q3": q3, "iqr": iqr,
            "lower_bound": lower, "upper_bound": upper, "flagged_rows": count
        })
    pd.DataFrame(outlier_report).to_csv(OUTPUT_DIR / "outlier_report.csv", index=False)

    df = df.sort_values("ObservationDate").reset_index(drop=True)
    output = OUTPUT_DIR / "covid_19_cleaned.csv"
    df.to_csv(output, index=False)

    print(f"\nCleaned shape: {df.shape}")
    print(f"Cleaned dataset saved to: {output}")
    print(f"Outlier report saved to: {OUTPUT_DIR / 'outlier_report.csv'}")
    print("\nCleaned missing values:\n", df.isna().sum())
    return df

if __name__ == "__main__":
    clean_data()
