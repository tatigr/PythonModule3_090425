# Дано произвольное предложение. Слова разделены пробелами. Предложение содержит знаки препинания.
# Найдите:
# 1) первое слово из строки
# 2) первые два символа каждого слова
# 3) все слова начинающиеся на гласную кириллическую букву
# 4) все слова начинающиеся на согласную кириллическую букву
# 5) все уникальные(без дубликатов) знаки препинания (знаками препинания считать символы .,!?;:)
import re

text = "Sed vestibulum laoreet a tellus; I vitae tincidunt odio euismod id. Nam!"

# 1) первое слово из строки
# template_task1 = r"^\w+\b"
# first_word = re.match(template_task1, text)
# print(first_word)

# 2) первые два символа каждого слова
template_task2 = r"\b\w{2}"
two_chars = re.findall(template_task2, text)
print(two_chars)
# import string
# 4) все слова начинающиеся на согласную латинскую букву
template_task4 = r"\b[BCDFGHJKLMNPQRSTVWXYZ]\w*"
words_consonant = re.findall(template_task4, text, re.IGNORECASE)
print(words_consonant)