# Сюда отправляем готовое решение IBank часть-3
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

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        # 400 * 1.02 -> 408
        amount_with_commission = int(amount * (Account.COMMISSION_PERCENT / 100 + 1))
        if amount_with_commission > self.__balance:
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


if __name__ == "__main__":
    account1 = Account("Алексей", "3232 456124", "+7-901-744-22-99", start_balance=1520)
    try:
        account1.withdraw(500)
    except ValueError as e:
        print(e)

    try:
        account1.withdraw(300)
    except ValueError as e:
        print(e)

    print(account1.balance)

    for operation in account1.get_history():
        print(operation)