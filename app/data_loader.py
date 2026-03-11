import pandas as pd
import os

def load_sales_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    file_path = os.path.join(base_dir, "data", "sales.csv")

    df = pd.read_csv(file_path)

    return df