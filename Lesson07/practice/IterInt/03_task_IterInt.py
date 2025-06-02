
class MyIterator:
    def __init__(self, number):
        self.number = number  # 123
        self.length = 0
        number = self.number
        while number != 0:
            number //= 10
            self.length += 1

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        digit = self.number // 10 ** (self.length - 1)
        self.number = self.number % 10 ** (self.length - 1)
        self.length -= 1
        return digit


class IterInt(int):
    def __iter__(self):
        return MyIterator(self)

    def __len__(self):
        return len(str(self))


# Найти наибольшую цифру в числе, используя итерацию по цифрам IterInt.
n = IterInt(123)

# max_digit = max(n)
num_digits = len(n)  # n.__len__()

print(num_digits)