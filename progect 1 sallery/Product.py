class Product:
    """
    Descriptions product
    """
    def __init__(self, name, prise: (int | float), descriptions = ''):
        self.name = name
        self.prise = prise
        self.descriptions = descriptions

    def __str__(self):
        return f'{self.name} {self.prise} uan'