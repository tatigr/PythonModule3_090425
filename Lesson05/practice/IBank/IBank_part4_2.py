# Сюда отправляем готовое решение IBank часть-4
class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, type, amount, target_account=None, commission=0):
        self.type = type
        self.amount = amount
        self.target_account = target_account
        self.commission = commission

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        str_out = f"{self.type} {self.amount} руб. (комиссия: {int(self.amount*self.commission/100)} руб.)"
        if self.type == Operation.TRANSFER_OUT:
            str_out += f" на счет клиента: {self.target_account.name}"
        if self.type == Operation.TRANSFER_IN:
            str_out += f" со счета клиента: {self.target_account.name}"
        return str_out


class Account:
    COMMISSION_PERCENT = 2
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        # историю храним как список объектов класса Operation, добавив свойство в конструктор:
        self.__history: list[Operation] = []

    @property
    def balance(self) -> int:
        return self.__balance

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"


    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб"


    # Данный метод дан в готовом виде. Изучите его и используйте как пример, для доработки других
    def deposit(self, amount: int, to_history: bool = True) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        :param to_history: True - записывать операцию в историю, False - не записывать
        """
        self.__balance += amount
        if to_history:
            operation = Operation(amount=amount, type=Operation.DEPOSIT)
            self.__history.append(operation)

    def _enough_money(self, amount) -> bool:
        return amount < self.__balance

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        amount_with_commission = int(amount * (Account.COMMISSION_PERCENT / 100 + 1))
        if not self._enough_money(amount_with_commission):
            raise ValueError("Недостаточно средств")

        self.__balance -= amount_with_commission
        if to_history:
            operation = Operation(amount=amount, type=Operation.WITHDRAW, commission=Account.COMMISSION_PERCENT)
            self.__history.append(operation)

    def transfer(self, target_account: 'Account', amount: int, to_history: bool = True) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, to_history=False)
        target_account.deposit(amount, to_history=False)

        if to_history:
            # Деньги ушли ->
            operation_out = Operation(
                amount=amount,
                type=Operation.TRANSFER_OUT,
                target_account=target_account,
                commission=Account.COMMISSION_PERCENT
            )
            # Деньги поступили <-
            operation_in = Operation(amount=amount, type=Operation.TRANSFER_IN, target_account=self)
            self.__history.append(operation_out)
            target_account.__history.append(operation_in)


    def get_history(self) -> list[Operation]:
        """
        :return: возвращаем историю операций в виде списка операций
        """
        return self.__history


class CreditAccount(Account):
    def __init__(self, name, passport, phone_number, start_balance=0, negative_limit=0):
        Account.__init__(self, name, passport, phone_number, start_balance)
        self.negative_limit = negative_limit

    def _enough_money(self, amount) -> bool:
        return amount < self.balance + self.negative_limit


if __name__ == "__main__":
    pass