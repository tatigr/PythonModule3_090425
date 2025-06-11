import sqlite3

connect = sqlite3.connect("task.db")
cursor = connect.cursor()

sql = """
SELECT ProductName, Price
FROM Products
WHERE ProductName NOT IN ('Монитор 27 дюймов', 'Ноутбук XYZ Pro') AND Price > 10000;
"""

cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connect.close()