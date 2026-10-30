from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def mode(self):
        pass


class Online(Payment):
    def mode(self):
        print("paid via cash")


class Cash(Payment):
    def mode(self):
        print("paid online")


class Order:
    def ordered(self, pay):
        pay.mode()


online = Online()
order = Order()
order.ordered(online)


class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass


class CardPay(PaymentGateway):
    def pay(self):
        print("Paid using Card")


class UpiPay(PaymentGateway):
    def pay(self):
        print("Paid using UPI")


class Purchase:
    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("Checkout started")
        self.gateway.pay()


p1 = Purchase(CardPay())
p2 = Purchase(UpiPay())

p1.checkout()
p2.checkout()
