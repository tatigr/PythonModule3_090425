# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y

# Рассмотрим самый простой случай для сложения дробей с целыми частями:
import re

simple_expression = "6 1/8 + 120 17/42"
simple_pattern = r"(\d+)\s+(\d+)/(\d+)\s*\+\s*(\d+)\s+(\d+)/(\d+)"

match = re.match(simple_pattern, simple_expression)

if match:
    print(match.groups())
else:
    print("Incorrect expression")
