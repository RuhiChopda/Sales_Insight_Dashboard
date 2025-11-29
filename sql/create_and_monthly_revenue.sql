-- sample SQL to create a sales table and aggregate monthly revenue
CREATE TABLE sales (
  order_id INTEGER PRIMARY KEY,
  order_date DATE,
  region TEXT,
  product_category TEXT,
  units_sold INTEGER,
  unit_price REAL,
  discount REAL,
  sales_amount REAL
);

-- Example: monthly revenue by region
SELECT strftime('%Y-%m', order_date) AS month, region, SUM(sales_amount) AS revenue
FROM sales
GROUP BY month, region
ORDER BY month;
