"""
Observer Pattern.

Permite definir un mecanismo de suscripción para
notificar a multiples objetos acerca de cualquier evento
que le suceda al objeto que estén observando.

Los objetos son capaces de suscribirse a una serie de 
eventos que otro objeto va a emitir, y serán avisados cuando
esto ocurra.

Permite definir un mecanismo de suscripción para notificar a varios objetos
sobre cualquier evento que le suceda al objeto que está siendo observado.
"""

from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer):
        raise NotImplementedError()

    @abstractmethod
    def unsubscribe(self, observer):
        raise NotImplementedError()

    @abstractmethod
    def notify(self):
        raise NotImplementedError()



class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        raise NotImplementedError()


class Motorcyle(Subject):
    
    __observers: List[Observer] = []
    price: int = 0

    def subscribe(self, observer):
        print(f"A new observer has been subscribed. {observer}.")
        self.__observers.append(observer)

    def unsubscribe(self, observer):
        print(f"A new observer has been unsubscribed. {observer}.")
        self.__observers.remove(observer)

    def notify(self):
        print(f"Notifyin to all observers....")
        for observer in self.__observers:
            observer.update(self)

    def change_price(self, price: int):
        print("The motorcycle price has been changed to {self.price}")
        self.price = price
        self.notify()


class Luisito(Observer):
    def update(self, subject):
        print(f"Luisito: The price of motorcycle has been chaged to{subject.price}.")


class Paquito(Observer):
    def update(self, subject):
        print(f"Paquito: The price of motorcycle has been change to. {subject.price}")


def main():

    motorcycle = Motorcyle()

    luisito = Luisito()
    paquito = Paquito()

    motorcycle.subscribe(luisito)
    motorcycle.subscribe(paquito)

    motorcycle.change_price(100000)

    motorcycle.unsubscribe(paquito)

    motorcycle.change_price(50000)


if __name__ == "__main__":
    main()












