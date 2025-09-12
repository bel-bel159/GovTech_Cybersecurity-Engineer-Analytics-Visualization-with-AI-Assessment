.headers on
.mode column
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
