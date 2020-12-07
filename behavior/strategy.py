"""
* Strategy Patterns *

"""
class Order:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount
    
    def __repr__(self):
        return repr(f"{self.__class__.__name__}")

# create strategies
def ten_percent_discount(order: Order):
    return order.price * 0.10

def on_sale_discount(order: Order):
    return order.price * 0.25 + 20


def main():
    # create an order without discount strategy
    order_1 = Order(100)
    print(order_1)

    # create an order with ten_percent strategy
    order_2 = Order(100, discount_strategy=ten_percent_discount)
    print(order_2)

    # create an order with on_sale_strategy
    order_3 = Order(1000, discount_strategy=on_sale_discount)
    print(order_3)

if __name__ == '__main__':
    main()

