import sqlite3

connect = sqlite3.connect("task.db")
cursor = connect.cursor()

product_name = "Монитор 27 дюймов"
product_price = 18400
product_quantity = 30

sql = """
INSERT INTO Products (ProductName, Price, StockQuantity) VALUES
(?, ?, ?);
"""

try:
    cursor.execute(sql, (product_name, product_price, product_quantity))
    connect.commit()
except sqlite3.OperationalError as e:
    print(f"Произошла ошибка: {e}")

cursor.close()
connect.close()