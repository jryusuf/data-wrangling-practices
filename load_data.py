import csv
import psycopg2
import os

db_host = "localhost"
db_name = "commerce"
db_user = "yusuf"
db_password = "password"
db_port = "5432"

conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password, port=db_port)
cursor = conn.cursor()

csv_files = [
    {"file": "customer_purchases.csv", "table": "customer_purchases", "columns": ["customer_id", "purchase_date", "product_id", "quantity", "country"], "types": ["INTEGER", "DATE", "VARCHAR(50)", "INTEGER", "VARCHAR(100)"]},
    {"file": "product_price.csv", "table": "product_prices", "columns": ["product_id", "price", "valid_from", "valid_to", "is_active"], "types": ["VARCHAR(50)", "DECIMAL", "DATE", "DATE", "INTEGER"], "date_columns": ["valid_from", "valid_to"]}]

for file_info in csv_files:
    table_name = file_info["table"]
    columns_def = ", ".join([f"{col} {file_info['types'][i]}" for i, col in enumerate(file_info["columns"])])

    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})")

    with open(file_info["file"], 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cols = ", ".join(file_info["columns"])
            vals = ", ".join(['%s'] * len(file_info["columns"]))
            sql = f"INSERT INTO {table_name} ({cols}) VALUES ({vals})"

            # Handle empty date strings
            row_values = []
            for col in file_info["columns"]:
                value = row[col]
                if col in file_info.get("date_columns", []) and value == "": # Check if column is a date column and value is empty
                    row_values.append(None) # Set to None for NULL in postgres
                else:
                    row_values.append(value)
            cursor.execute(sql, row_values)
    conn.commit()
    print(f"Loaded {file_info['file']} to {table_name}")

cursor.close()
conn.close()
print("Done")