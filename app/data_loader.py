import pandas as pd
import os

def load_sales_data():
    # Get root project directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # CSV file location
    csv_path = os.path.join(base_dir, "data", "sales.csv")

    # Load data
    df = pd.read_csv(csv_path)

    return df