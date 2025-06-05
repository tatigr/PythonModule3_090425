# Найти в строке все последовательности, состоящие ровно из 4 цифр подряд.
import re

string = "Номера: 12345, 9876, 0000, 12."
pattern = r"\b\d{4}\b"

regexp = re.compile(pattern)
numbers = regexp.findall(string)

print(numbers)
