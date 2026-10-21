"""Create at least six visualizations from the cleaned COVID-19 dataset."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
CLEAN_FILE = ROOT / "data" / "processed" / "covid_19_cleaned.csv"
GRAPH_DIR = ROOT / "graphs"
GRAPH_DIR.mkdir(parents=True, exist_ok=True)
sns.set_theme(style="whitegrid")

def create_visualizations():
    if not CLEAN_FILE.exists():
        raise FileNotFoundError("Cleaned data not found. Run main.py or data_cleaning.py first.")
    df = pd.read_csv(CLEAN_FILE, parse_dates=["ObservationDate"])
    for col in ["Confirmed", "Deaths", "Recovered"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    df["Country_Region"] = df["Country_Region"].fillna("Unknown")

    # For cumulative counts, aggregate locations for each observation date.
    daily = df.groupby("ObservationDate", as_index=False)[["Confirmed", "Deaths", "Recovered"]].sum()

    # 1. Confirmed cases over time
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=daily, x="ObservationDate", y="Confirmed")
    plt.title("Global Reported Confirmed COVID-19 Cases Over Time")
    plt.xlabel("Observation date"); plt.ylabel("Reported confirmed cases")
    plt.tight_layout(); plt.savefig(GRAPH_DIR / "01_confirmed_cases_over_time.png", dpi=160); plt.close()

    # 2. Deaths over time
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=daily, x="ObservationDate", y="Deaths")
    plt.title("Global Reported COVID-19 Deaths Over Time")
    plt.xlabel("Observation date"); plt.ylabel("Reported deaths")
    plt.tight_layout(); plt.savefig(GRAPH_DIR / "02_deaths_over_time.png", dpi=160); plt.close()

    # 3. Recoveries over time
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=daily, x="ObservationDate", y="Recovered")
    plt.title("Global Reported COVID-19 Recoveries Over Time")
    plt.xlabel("Observation date"); plt.ylabel("Reported recoveries")
    plt.tight_layout(); plt.savefig(GRAPH_DIR / "03_recoveries_over_time.png", dpi=160); plt.close()

    # Use the latest available observation per country for country comparisons.
    latest_date = df["ObservationDate"].max()
    latest = df[df["ObservationDate"] == latest_date].groupby("Country_Region", as_index=False)[
        ["Confirmed", "Deaths", "Recovered"]
    ].sum()
    top = latest.sort_values("Confirmed", ascending=False).head(10)

    # 4. Top ten countries by confirmed cases
    plt.figure(figsize=(11, 6))
    sns.barplot(data=top.sort_values("Confirmed"), x="Confirmed", y="Country_Region")
    plt.title(f"Top 10 Countries by Reported Confirmed Cases ({latest_date.date()})")
    plt.xlabel("Reported confirmed cases"); plt.ylabel("Country/Region")
    plt.tight_layout(); plt.savefig(GRAPH_DIR / "04_top_10_countries.png", dpi=160); plt.close()

    # 5. Comparison of confirmed, deaths and recoveries in the top countries
    long = top.melt(id_vars="Country_Region", value_vars=["Confirmed", "Deaths", "Recovered"],
                    var_name="Measure", value_name="Reported count")
    plt.figure(figsize=(12, 6))
    sns.barplot(data=long, x="Country_Region", y="Reported count", hue="Measure")
    plt.title(f"Reported Cases, Deaths and Recoveries in Top Countries ({latest_date.date()})")
    plt.xlabel("Country/Region"); plt.ylabel("Reported count")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout(); plt.savefig(GRAPH_DIR / "05_country_comparison.png", dpi=160); plt.close()

    # 6. Distribution of confirmed cases among the top 15 countries
    top15 = latest.sort_values("Confirmed", ascending=False).head(15).sort_values("Confirmed")
    plt.figure(figsize=(11, 6))
    sns.barplot(data=top15, x="Confirmed", y="Country_Region")
    plt.title(f"Distribution of Reported Confirmed Cases: Top 15 Countries ({latest_date.date()})")
    plt.xlabel("Reported confirmed cases"); plt.ylabel("Country/Region")
    plt.tight_layout(); plt.savefig(GRAPH_DIR / "06_case_distribution_top_15.png", dpi=160); plt.close()

    # Save a small machine-generated summary to support the insights report.
    top3 = latest.sort_values("Confirmed", ascending=False).head(3)
    with open(ROOT / "insights.md", "w", encoding="utf-8") as f:
        f.write("# COVID-19 Data Insights\n\n")
        f.write(f"- Latest observation date in the dataset: **{latest_date.date()}**.\n")
        f.write(f"- Number of countries/regions in the latest observation: **{latest['Country_Region'].nunique()}**.\n")
        f.write("- Top countries by reported confirmed cases in the latest observation:\n")
        for _, row in top3.iterrows():
            f.write(f"  - **{row['Country_Region']}**: {row['Confirmed']:,.0f} confirmed, "
                    f"{row['Deaths']:,.0f} deaths, {row['Recovered']:,.0f} recovered.\n")
        f.write("\nThese are descriptive summaries of the dataset, not estimates of current infections. "
                "Reported cumulative counts, data quality, and differences in reporting should be considered.\n")

    print(f"Created 6 graphs in: {GRAPH_DIR}")
    print(f"Generated insights report: {ROOT / 'insights.md'}")

if __name__ == "__main__":
    create_visualizations()
