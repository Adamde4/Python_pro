class Customer:
    def __init__(self, name, surname, telephone):
        self.name = name
        self.surname = surname
        self.telephone = telephone

    def __str__(self):
        return f'{self.surname} {self.name}, {self.telephone}'