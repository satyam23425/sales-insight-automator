from fastapi import FastAPI
from app.data_loader import load_sales_data
from app.analyzer import total_sales, sales_by_product, sales_by_region, top_product

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sales Insight Automator Running on Vercel"}

@app.get("/insights")
def insights():
    df = load_sales_data()

    return {
        "total_sales": total_sales(df),
        "sales_by_product": sales_by_product(df),
        "sales_by_region": sales_by_region(df),
        "top_product": top_product(df)
    }