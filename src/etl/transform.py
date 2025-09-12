import pandas as pd

# prepares the sales dataset, making it clean and doing the tasked items :
# 1. join orders with products
# 2. calculate revenue
# 3. derive the orderyear, ordermonth, orderday
# 4. additional task is to create the DateKey in yyyymmdd format to uniquely identify each date so that joining and indexing will be faster
def prepare_sales_data(df_orders: pd.DataFrame,
                       df_products: pd.DataFrame) -> pd.DataFrame:
    
    # 1. Join orders with products (left join so that every line of order will be kept)
    df = df_orders.merge(df_products, on="ProductID", how="left")

    # 2. Calculate revenue
    df["Revenue"] = df["Quantity"] * df["Price"]

    # 3. Derive year/month/day
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    df["OrderYear"]  = df["OrderDate"].dt.year
    df["OrderMonth"] = df["OrderDate"].dt.month
    df["OrderDay"]   = df["OrderDate"].dt.day

    # 4. DateKey for DimDate join
    df["DateKey"] = df["OrderDate"].dt.strftime("%Y%m%d").astype(int)

    return df
