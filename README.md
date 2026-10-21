# COVID-19 Data Analysis and Visualization

## 1. Project Overview

**Project Name:** COVID-19 Data Analysis and Visualization  
**Group Name:** Psquare  
**Domain:** Python, Data Analysis and Data Visualization

This project analyzes the Novel Coronavirus 2019 dataset using Python. It focuses on cleaning and preprocessing COVID-19 data, exploring trends in confirmed cases, deaths, and recoveries, and presenting findings through meaningful visualizations.

The project demonstrates how Python libraries can be used to process real-world data and extract useful information from it.

## 2. Dataset Information

**Dataset Name:** Novel Corona Virus 2019 Dataset

**Dataset Source:** [Kaggle - Novel Corona Virus 2019 Dataset](https://www.kaggle.com/datasets/sudalairajkumar/novel-corona-virus-2019-dataset)

The dataset contains historical COVID-19 records, including observation dates, geographical information, confirmed cases, deaths, and recoveries.

## 3. Project Objectives

- Load and explore the COVID-19 dataset using Pandas.
- Identify and handle missing values.
- Detect and remove duplicate records where appropriate.
- Correct data types and investigate outliers.
- Analyze COVID-19 trends over time and across countries.
- Create at least six data visualizations.
- Prepare a short report summarizing the findings.

## 4. Technologies and Libraries Used

- **Python:** Main programming language.
- **Pandas:** Data loading, cleaning, and manipulation.
- **NumPy:** Numerical operations.
- **Matplotlib:** Data visualization.
- **Seaborn:** Statistical visualization.
- **Git and GitHub:** Version control and team collaboration.
- **Jupyter Notebook / VS Code:** Development environment.

## 5. Project Structure

```text
COVID-19-Data-Analysis-and-Visualization/
│
├── data/
│   └── covid_19_data.csv
├── graphs/
│   ├── confirmed_cases_over_time.png
│   ├── deaths_over_time.png
│   ├── recoveries_over_time.png
│   ├── top_countries.png
│   ├── country_comparison.png
│   └── case_distribution.png
├── data_cleaning.py
├── visualizations.py
├── main.py
├── requirements.txt
├── insights.md
├── CONTRIBUTIONS.md
└── README.md
```

*Note: This structure describes the intended organization. The files and graph names should match the actual files committed to the repository.*

## 6. Data Cleaning and Preprocessing

The following data-cleaning tasks are included in the project:

1. Inspect the dataset's rows, columns, and data types.
2. Identify missing values and handle them using appropriate methods.
3. Detect duplicate records and remove only inappropriate duplicates.
4. Convert date columns into the correct date format.
5. Convert numerical columns into suitable numeric data types.
6. Investigate outliers and decide how to handle them based on the data.
7. Verify the cleaned dataset before visualization.

## 7. Data Visualizations

At least six visualizations will be created:

1. **Confirmed Cases Over Time:** Shows the trend in reported confirmed cases.
2. **Deaths Over Time:** Shows the trend in reported deaths.
3. **Recoveries Over Time:** Shows the trend in reported recoveries.
4. **Top 10 Countries by Confirmed Cases:** Compares countries with high reported case counts.
5. **Country-wise Case Comparison:** Compares confirmed cases, deaths, and recoveries across selected countries.
6. **Distribution of Confirmed Cases:** Shows how reported cases are distributed across countries.

The graphs will be saved in the `graphs/` folder and interpreted in the insights report.

## 8. Tools and Methodology

The project follows these steps:

1. Download the dataset from Kaggle.
2. Load the CSV file into Pandas.
3. Explore and clean the data.
4. Perform analysis on dates, countries, confirmed cases, deaths, and recoveries.
5. Generate and save visualizations.
6. Interpret the findings.
7. Document the code, methodology, and results in GitHub.

## 9. Key Insights

This section will be completed after running the analysis.

The report will describe:

- Changes in reported confirmed cases over time.
- Trends in reported deaths and recoveries.
- Countries with the highest confirmed case counts in the selected period.
- Differences between countries in reported cases, deaths, and recoveries.
- Data-quality issues and limitations identified during preprocessing.

All findings will be based on the actual analysis results.

## 10. How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/palakchavda34-maker/COVID-19-Data-Analysis-and-Visualization.git
cd COVID-19-Data-Analysis-and-Visualization
```

### Step 2: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 3: Add the dataset

Download the dataset from Kaggle and place the required CSV file in the `data/` folder. Ensure the filename matches the one used in the code.

### Step 4: Run the project

```bash
python main.py
```

The script should execute the cleaning and visualization workflow and save the resulting graphs in the `graphs/` folder.

## 11. Team Members and Contributions

### Member 1: Palak Chavda - IU2441230599

- Dataset exploration and data cleaning.
- Missing-value and duplicate handling.
- Data-type correction and outlier investigation.
- Development and testing of the data-cleaning module.

### Member 2: Pari Shah - IU2441230647

- Development of visualization functions.
- Creation of at least six graphs.
- Country-wise and time-series analysis.
- Preparation of the insights report.

Both members will contribute to testing, documentation, and final integration. Individual contributions will be documented through GitHub commits and pull requests.

## 12. Conclusion

This project demonstrates the use of Python for cleaning, analyzing, and visualizing COVID-19 data. It provides practical experience in data preprocessing, exploratory data analysis, graphical representation, and collaborative software development using GitHub.

The project aims to present historical COVID-19 data in a clear and understandable form while recognizing the limitations of the available dataset.

## 13. References

1. [Novel Corona Virus 2019 Dataset - Kaggle](https://www.kaggle.com/datasets/sudalairajkumar/novel-corona-virus-2019-dataset)
2. [Pandas Documentation](https://pandas.pydata.org/docs/)
3. [NumPy Documentation](https://numpy.org/doc/)
4. [Matplotlib Documentation](https://matplotlib.org/stable/)
5. [Seaborn Documentation](https://seaborn.pydata.org/)
6. [GitHub Documentation](https://docs.github.com/)
