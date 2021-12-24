from Customer import Customer
from Product import Product
from Order import Order

if __name__=='__main__':
    x = Product('apple', 25)
    y = Product('banana', 28)
    z = Product('orange', 30)

    customer_1 = Customer('Ivan', 'Ivanov', 380730228841)
    customer_2 = Customer('Volodimir', 'Lenin', 380735555541)

    order_1 = Order(customer_1, [x, y, y, z])
    order_2 = Order(customer_2, [y, z, z])

    print(order_1)
    print(order_2)