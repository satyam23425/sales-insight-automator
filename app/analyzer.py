import pandas as pd

def total_sales(df):
    return df["sales"].sum()

def sales_by_product(df):
    return df.groupby("product")["sales"].sum().to_dict()

def sales_by_region(df):
    return df.groupby("region")["sales"].sum().to_dict()

def top_product(df):
    result = df.groupby("product")["sales"].sum()
    return result.idxmax()