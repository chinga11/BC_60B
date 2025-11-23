import random
from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance
        self.__password = password
        self.notifier = None

    def __generate_pin(self):
        return random.randint(0, 9999)

    def deposit(self, amount, password):
        if password != self.__password:
            return "Неверный пароль!"
        self._balance += amount
        return self._balance

    def withdraw(self, amount, password):
        if password != self.__password:
            return "Неверный пароль!"
        if self._balance < amount:
            return "Недостаточно средств!"
        self._balance -= amount
        return self._balance

    def change_password(self, old_password, new_password):
        if old_password != self.__password:
            return "Старый пароль неверный"
        self.__password = new_password
        return "Пароль изменён"

    def get_balance(self, password):
        if password != self.__password:
            return "Неверный пароль!"
        return self._balance

    def reset_pin(self, password):
        if password != self.__password:
            return "Неверный пароль!"
        new_pin = self.__generate_pin()
        self.__password = new_pin
        return new_pin


class NotificationSender(ABC):

    @abstractmethod
    def send(self, message, recipient):
        pass

    def get_service(self):
        return f"Сервис: {self._service}"


class EmailSender(NotificationSender):
    def __init__(self):
        self._service = "Gmail"

    def send(self, message, recipient):
        return f"Email sent to {recipient}"


class SmsSender(NotificationSender):
    def __init__(self):
        self._service = "Twilio"

    def send(self, message, recipient):
        return f"SMS sent to {recipient}"


class PushSender(NotificationSender):
    def __init__(self):
        self._service = "Firebase"

    def send(self, message, recipient):
        return f"Push sent to {recipient}"

class UserAuth:
    def __init__(self, username, account: BankAccount, notifier: NotificationSender):
        self.username = username
        self.account = account
        self.notifier = notifier
        self.account.notifier = notifier

    def login(self, password):
        if isinstance(self.account.get_balance(password), int):
            print(self.notifier.send(f"Успешный вход: {self.username}", "номер или почта"))
            return True
        else:
            return False

    def transfer(self, amount, password, recipient_account: BankAccount):
        withdrawal_result = self.account.withdraw(amount, password)
        if isinstance(withdrawal_result, str):
            return f"Перевод не выполнен: {withdrawal_result}"
        recipient_account._balance += amount

        print(self.notifier.send(f"Перевод {amount} отправлен", "system"))
        if recipient_account.notifier:
            print(recipient_account.notifier.send(f"Получено {amount} от {self.username}", "system"))
        return f"Перевод успешен. Новый баланс: {self.account._balance}"


john = BankAccount("John", 100, "123qwerty")
print(john.deposit(50, "123qwerty"))
print(john.deposit(100, "123qwerty"))
print(john.withdraw(100, "123qwerty"))
print(john.get_balance("123qwerty"))
print(john.change_password("wrong", "new"))
print(john.change_password("123qwerty", "new"))
print(john.reset_pin("new"))
print(john.get_balance("5832"))

email = EmailSender()
sms = SmsSender()
print(email.send("Привет", "test@mail.ru"))
print(email.get_service())
print(sms.get_service())

john_acc = BankAccount("John", 150, "secret")
alice_acc = BankAccount("Alice", 50, "pass123")
notifier = SmsSender()
auth = UserAuth("john_doe", john_acc, notifier)
auth_alice = UserAuth("alice_smith", alice_acc, notifier)
auth.login("secret")
transfer_result = auth.transfer(70, "secret", alice_acc)
print(transfer_result)
print(f"John balance: {john_acc._balance}")
print(f"Alice balance: {alice_acc._balance}")
