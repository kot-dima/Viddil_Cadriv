from incl import *

class Dev (Incluid):
    def __init__(self, name: str, surname: str, age: int, posada: str, price: int, skills: str):
        Incluid.__init__(self, name, surname, age, posada, price)
        self.__skills = skills

    def show_person_info(self):
        print("Name: ", self.name, "\nSurname: ", self.surname, "\nAge: ",
              self.age, "\nPosition: ", "\nSkills: ", self.__skills)


dev = Dev("Adam", "Dobson", 23, "Posada", 13000, "Skils")

dev.show_person_info()
dev.name = "Adamus"
dev.surname = "Dobsunos"
dev.age = 24
dev.posada = "Posada 1"
dev.price = 10000
dev.skils = "Skills 1"
dev.show_person_info()
