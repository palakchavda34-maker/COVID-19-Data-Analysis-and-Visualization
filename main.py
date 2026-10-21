"""Run the complete COVID-19 cleaning and visualization workflow."""
from data_cleaning import clean_data
from visualizations import create_visualizations

def main():
    clean_data()
    create_visualizations()
    print("\nProject completed. Check the graphs/ folder and insights.md.")

if __name__ == "__main__":
    main()
