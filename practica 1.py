#part 1
class empl:

    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f'{self.surname} {self.name}'

class department:
    def __init__(self, name_dep, empl:list):
        self.name_dep = name_dep
        self.empl = empl

    def add_empl(self, empl):
        self.empl.append(empl)

    def remove_empl(self, remove):
        self.empl.remove(empl)


    def __str__(self):
        res = '\n'.join(map(str, self.empl))
        return f'{self.name_dep}\n{res}'

empl_1 = empl('John', 'Mactavish', '01.01.1980')
empl_2 = empl('Sherlock', 'Holms', '01.01.1980')
empl_3 = empl('Victor', 'Reznov', '01.01.1980')

dep_1 = department('Offiss', [empl_1, empl_2, empl_3])
print(dep_1)

#part 2
class rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return 'rectangle [a = '+str(self.a)+', b = '+str(self.b)+']'

rectangle_1 = rectangle(4, 5)
print(rectangle_1)
print(rectangle_1.get_area())