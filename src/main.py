from pathlib import Path
from utils.db import init_schema
from etl import extract_data, prepare_sales_data, load_all

# Runs the full pipeline : 
# 1. Create / Recreate the database schema
# 2. Extract the data from the CSV, orders and products
# 3. Transform and enrich the data extracted
# 4. Load the data into the SQLite data warehouse
def main():
    # Set input file paths
    base_dir = Path(__file__).resolve().parent
    dataset_dir = base_dir / "dataset"
    orders_file   = dataset_dir / "orders.csv"
    products_file = dataset_dir / "products.csv"

    # 1. Create / Recreate the database schema
    init_schema()

    # 2. Extract raw data
    orders_df, products_df = extract_data(orders_file, products_file)

    # 3. Transform: join, compute Revenue and Date fields
    sales_ready_df = prepare_sales_data(orders_df, products_df)

    # 4. Load into the SQLite database
    load_all(sales_ready_df, products_df)

    print("ETL complete — data warehouse created at output/sales_dw.sqlite")

if __name__ == "__main__":
    main()
