# Проверить, состоит ли вся строка полностью только из букв (латинских, строчных или прописных).
import re

string = "hell!oworldhiby"

regexp = re.compile(r"[A-Z]+", re.IGNORECASE)

result = regexp.fullmatch(string)
if result:
    print("Строка соответствует шаблону")
else:
    print("Строка НЕ соответствует шаблону")