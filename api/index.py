@app.get("/insights")
def insights():
    return {
        "total_sales": 4600,
        "sales_by_product": {
            "Laptop": 2100,
            "Phone": 1400,
            "Tablet": 1100
        },
        "sales_by_region": {
            "North": 2000,
            "South": 1600,
            "West": 600,
            "East": 400
        },
        "top_product": "Laptop"
    }