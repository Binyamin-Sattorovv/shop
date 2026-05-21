from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):

        pass


class ClickPayment(Payment):

    def pay(self, amount):

        return (
            f"Click payment kabul shud!\n"
            f"Summa: {amount} somoni\n"
        )


class CardPayment(Payment):

    def pay(self, amount):

        return (
            f"Card payment kabul shud!\n"
            f"Summa: {amount} somoni\n"
        )


class CashPayment(Payment):

    def pay(self, amount):

        return (
            f"Cash payment kabul shud!\n"
            f"Summa: {amount} somoni\n"
        )