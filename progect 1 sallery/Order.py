from Customer import Customer
from Product import Product

class Order:
    def __init__(self, customer: Customer, products=None):
        self.customer = customer
        self.__products = products

    def __str__(self):
        res = '\n\t'.join(map(str, self.__products))
        return f'{self.customer}\n{res}\n\tTotal price: {self.total_prise()}'

    def total_prise(self):
        s = 0
        for element in self.__products:
            s += element.prise
        return s

    def add_product(self, value: Product):
        if isinstance(value, Product):
            self.__products.appends(value)

    def remove_product(self, value):
        if value in self.__products:
            self.__products.remove(value)