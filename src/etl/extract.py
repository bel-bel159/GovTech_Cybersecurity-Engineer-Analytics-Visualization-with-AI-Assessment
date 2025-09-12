from pathlib import Path
import pandas as pd

# reads the 2 csv file, orders and products, and returning them in dataframes
def extract_data(orders_path: Path, products_path: Path):
    orders = pd.read_csv(orders_path)
    products = pd.read_csv(products_path)
    return orders, products
