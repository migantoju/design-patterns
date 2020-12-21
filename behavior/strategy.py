"""
* Strategy Pattern *

Es un patrón de diseño de comportamiento, que permite definir una seria o familia de algoritmos, encapsularlos en clases separadas y hacerlos
intercambiables.

Nos permite solucionar un problema de diferentes maneras.

*PROS*
- Obedece el principio SOLID *Open/Closed*, ya que es fácil introducir nuevas
  estrategias sin la necesidad de cambiar el código del cliente.

*CONS*
- Incrementa la complejidad, cuando únicamente tenemos un número pequeño de
  algoritmos/estrategias a implementar, entonces se vuelve ineficiente
  implementar este patrón.

*Aplicación*
- Clases similares, este método es altamente recomendado cuando tenemos muchas
  clases similares pero  que difieren en la manera en que se ejecutan.
"""
class Order:
    def __init__(self, price, strategy=None):
        self.price = price
        self.strategy = strategy

    def price_after_discount(self):
        if self.strategy:
            discount = self.strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self):
        return repr(f"Price: {self.price}, Price after discount: {self.price_after_discount()}")


def ten_percent_discount(order: Order):
    return order.price * 0.10


def on_sale_discount(order: Order):
    return order.price * 0.15 + 20


def main():
    # order without discount
    order1 = Order(100)
    print(order1)

    # order with ten percent discount
    order2 = Order(100, strategy=ten_percent_discount)
    print(order2)

    # order on sale discount
    order3 = Order(1000, strategy=on_sale_discount)
    print(order3)


if __name__ == "__main__":
    main()





