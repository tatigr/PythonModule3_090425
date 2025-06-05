# Проверить, начинается ли заданная строка с фразы "Начало:".
import re

string = "Еще Начало нового предложения."
pattern = r"Начало"
regexp = re.compile(pattern)
match = regexp.match(string)

if match:
    print(f"Строка начинается со слова Начало")
else:
    print(f"Строка НЕ начинается со слова Начало")