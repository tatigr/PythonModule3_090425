# Задание "Упрощение дроби"
import re
import math

def parse_fraction(fraction: str) -> tuple | None:
    # fraction_pattern = r"(-?)(?:(\d+)\s+)?(\d+)/(\d+)"
    if fraction.find("/") == -1:
        whole_pattern = r"(-?)(\d+)"
        match = re.match(whole_pattern, fraction)
        return match.groups() + (None, None)
    fraction_pattern = r"(-?)(?:(\d+)\s+)?(?:(\d+)/(\d+))?"
    match = re.match(fraction_pattern, fraction)
    if match:
        return match.groups()
    return None


def simplificator(fraction: str) -> str:
    sign, whole, numerator, denominator = parse_fraction(fraction)
    numerator = int(numerator)
    denominator = int(denominator)
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return f"{sign}{whole} {numerator}/{denominator}"


# Простые дроби заданы в виде строки формата: целая_часть числитель/знаменатель
# целая_часть может отсутствовать, числитель и знаменатель всегда присутствуют
# если целая часть присутствует, то всегда отделяется от дробной пробелом
# дроби могут быть отрицательными или положительными
# Примеры дробей
fraction1 = "3 12/15"
fraction2 = "-1 11/6"
fraction3 = "2/4"
fraction4 = "-5/4"

# TODO: Задание: Напишите функцию simplificator, которая возвращает дробь в упрощенном виде с выделением целой части
print(simplificator("3 12/15"))  # --> 3 4/5
# simplificator("-1 11/6")  # --> -2 5/6
# simplificator("2/4")  # --> 1/2
# simplificator("-5/4")  # --> -1 1/4

# Подсказки: смотри файл helpers/lcmp_gcd.py
