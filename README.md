# GovTech_Cybersecurity-Engineer-Analytics-Visualization-with-AI-Assessment

## Setup & How to Run

### Setup
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




