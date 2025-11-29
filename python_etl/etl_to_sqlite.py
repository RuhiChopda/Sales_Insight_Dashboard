import sqlite3, pandas as pd, pathlib
db_path = pathlib.Path(__file__).resolve().parents[1] / 'sales.db'
df = pd.read_csv(pathlib.Path(__file__).resolve().parents[1] / 'data' / 'sales_sample.csv', parse_dates=['order_date'])
conn = sqlite3.connect(db_path)
df.to_sql('sales', conn, if_exists='replace', index=False)
monthly = pd.read_sql_query("""SELECT strftime('%Y-%m', order_date) AS month, region, product_category, SUM(sales_amount) AS revenue FROM sales GROUP BY month, region, product_category""", conn)
monthly.to_csv(pathlib.Path(__file__).resolve().parents[1] / 'data' / 'monthly_revenue_for_powerbi.csv', index=False)
print('ETL complete. DB and summary CSV created:', db_path)
