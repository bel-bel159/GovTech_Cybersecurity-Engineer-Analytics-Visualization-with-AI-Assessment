from utils.db import get_connection
import datetime as dt

# load dimensions and fact table into SQLite
# schema has already been created in main.py through init_schema()
def load_all(df_sales, df_products):
    with get_connection() as conn:
        # Load DimProduct insert from df_products
        for _, row in df_products.iterrows():
            conn.execute("""
            INSERT INTO DimProduct (ProductID, ProductName, Category, Cost)
            VALUES (?, ?, ?, ?);
            """, (row["ProductID"],
                  row["ProductName"],
                  row["Category"],
                  float(row["Cost"])))

        # Load DimDate (unique dates from df_sales)
        for iso in sorted(df_sales["OrderDate"].dt.strftime("%Y-%m-%d").unique()):
            y, m, d = map(int, iso.split("-"))
            month_name = dt.date(y, m, d).strftime("%B")
            date_key = int(iso.replace("-", ""))
            conn.execute("""
            INSERT INTO DimDate
            (DateKey, FullDate, Year, Month, Day, MonthName)
            VALUES (?, ?, ?, ?, ?, ?);
            """, (date_key, iso, y, m, d, month_name))

        # Load FactSales with the productKey
        for _, row in df_sales.iterrows():
            # Get the productKey
            cur = conn.execute("SELECT ProductKey FROM DimProduct WHERE ProductID = ?",
                            (row["ProductID"],))
            product_key = cur.fetchone()[0]
            conn.execute("""
            INSERT INTO FactSales
            (OrderID, ProductKey, DateKey, CustomerID, Quantity, Price, Revenue)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (
                int(row["OrderID"]),
                product_key,
                int(row["DateKey"]),
                row["CustomerID"],
                int(row["Quantity"]),
                float(row["Price"]),
                float(row["Revenue"])
            ))
        conn.commit()
