# GovTech_Cybersecurity-Engineer-Analytics-Visualization-with-AI-Assessment

## Setup & How to Run

### Setup
Ensure that you have the following installed:
* **Python 3.10+**
* **pandas**
* **SQLite 3 CLI**

### How to Run
**To run the ETL pipeline**:
   ```bash
   cd src
   python main.py
   ```

**To run the SQL query to view table for 'total revenue for each product category for each month'**:
   ```bash
   sqlite3 output/sales_dw.sqlite ".read schema/query.sql"
   ```


## Data Model Description
I have created 2 dimension tables and 1 fact table, modelled as a simple star schema.

* Fact Table – `FactSales`

    | Column       | Type    | Description |
    |--------------|---------|------------|
    | OrderID      | INTEGER | Order line identifier |
    | ProductKey   | INTEGER | FK → DimProduct |
    | DateKey      | INTEGER | FK → DimDate |
    | CustomerID   | TEXT    | Customer identifier |
    | Quantity     | INTEGER | Quantity sold |
    | Price        | REAL    | Unit price |
    | Revenue      | REAL    | Quantity × Price |

    *FK - Foreign Key

* Dimension Table - `DimProduct`

    | Column          | Type                              | Description           |
    | --------------- | --------------------------------- | --------------------- |
    | **ProductKey**  | INTEGER PRIMARY KEY AUTOINCREMENT | Surrogate key         |
    | **ProductID**   | TEXT UNIQUE                       | Business product code |
    | **ProductName** | TEXT                              | Product name          |
    | **Category**    | TEXT                              | Product category      |
    | **Cost**        | REAL                              | Unit cost of product  |

* Dimension Table - `DimDate`

    | Column        | Type                           | Description               |
    | ------------- | ------------------------------ | ------------------------- |
    | **DateKey**   | INTEGER PRIMARY KEY (yyyymmdd) | Surrogate key for joining |
    | **FullDate**  | TEXT (ISO format)              | Complete calendar date    |
    | **Year**      | INTEGER                        | Year of order             |
    | **Month**     | INTEGER                        | Month number (1–12)       |
    | **Day**       | INTEGER                        | Day of month              |
    | **MonthName** | TEXT                           | Full month name           |

**Relationships**
Fact Sales is the central fact table where it links to DimProduct table through the ProductKey FK, and to DimDate through the DateKey FK, forming a simple star schema.

Surrogate Keys, ProductKey and DateKey enable joins between tables even if the business identifiers changed.


## Analytical Query (SQL):
The SQL query is to calculate the total revenue for each product category per month, this query is also stored in src/schema/query.sql . The query sorts the results by the numeric month for the calendar order.

```bash
SELECT
  d.Year,
  d.MonthName,
  p.Category,
  ROUND(SUM(f.Revenue), 2) AS TotalRevenue
FROM FactSales f
JOIN DimDate d     ON f.DateKey   = d.DateKey
JOIN DimProduct p  ON f.ProductKey = p.ProductKey
GROUP BY d.Year, d.MonthName, d.Month, p.Category
ORDER BY d.Year, d.Month, p.Category;
```


## Dashboarding Use Case:
* How your designed data model (FactSales, DimProduct, DimDate or similar) is suitable for efficient dashboarding.

    The designed data model is suitable for effective dashboarding since the fact table has only numeric values and FK entries, and the dimension tables store the descriptive values. This enable the dashboarding tools to:
    * Filter and slice quickly by product category, month or individual product from the DimProduct and DimDate tables without having to scan through raw dataset.
    * Group and sum the fact table based on its FK columns to produce Key Performance Indicator (KPI) with minimal computation.
    * Join the fact table to its dimension table to create new visualization without needing to redesign the schema.

* What are three key metrics or visualizations you would propose for this sales dashboard? Explain why each is important for understanding sales performance.

    * **Monthly Revenue by Category**  
        Even though this is suggested for the SQL query, it is still a good metric as it shows which category has the highest revenue and the trend of popularity of the category over time.

    * **Top products by Total Quantity Sold**  
        This is to identify which individual product has the highest quantity sold regardless of price which shows the product popularity and can help with promotional focus.

    * **Average Order Value Over Time**  
        This can indicate customer spending behaviour where high average order value means that customers are making big purchases per order over a period and low average order value means that customers are making small purchases per order. This is a good metric as it can show trends over different periods, for example, christmas period tend to have high average order as customers would want to purchase presents.
