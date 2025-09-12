DROP TABLE IF EXISTS FactSales;
DROP TABLE IF EXISTS DimDate;
DROP TABLE IF EXISTS DimProduct;

CREATE TABLE DimDate (
    -- yyyymmdd surrogate key
    DateKey   INTEGER PRIMARY KEY, 
    FullDate  TEXT    NOT NULL,
    Year      INTEGER NOT NULL,
    Month     INTEGER NOT NULL,
    Day       INTEGER NOT NULL,
    MonthName TEXT    NOT NULL
);

CREATE TABLE DimProduct (
    ProductKey  INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID   TEXT UNIQUE NOT NULL,
    ProductName TEXT NOT NULL,
    Category    TEXT NOT NULL,
    Cost        REAL NOT NULL
);

CREATE TABLE FactSales (
    SalesKey   INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderID    INTEGER NOT NULL,
    ProductKey INTEGER NOT NULL,
    DateKey    INTEGER NOT NULL,
    CustomerID TEXT    NOT NULL,
    Quantity   INTEGER NOT NULL,
    Price      REAL    NOT NULL,
    Revenue    REAL    NOT NULL,
    FOREIGN KEY(ProductKey) REFERENCES DimProduct(ProductKey),
    FOREIGN KEY(DateKey)   REFERENCES DimDate(DateKey)
);
