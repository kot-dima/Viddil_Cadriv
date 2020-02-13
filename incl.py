__id = 0

class Incluid:
    def __init__(self, name: str, surname: str, age: int, posada: str, price: int):
        self.__name: str = name
        self.__surname: str = surname
        self.___age: int = age
        self.__posada: str = posada
        self.__price: str = price

    def show_person_info(self):
        print("Name: ", self.__name, "\nSurname: ",
              self.__surname, "\nAge: ", self.__age, "\nAge: ",
              self.__posada, "\nAge: ", self.__price)

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @property
    def posada(self):
        return self.__posada

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @surname.setter
    def surname(self, new_surname: str):
        self.__surname = new_surname

    @age.setter
    def age(self, new_age: int):
        self.__age = new_age

    @posada.setter
    def posada(self, new_posada: str):
        self.__posada = new_posada

    @price.setter
    def price(self, new_price: int):
        self.__price = new_price
