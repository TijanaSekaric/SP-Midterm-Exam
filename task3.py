from abc import ABC, abstractmethod  # kada trazimo apsraktnu klasu uvijek pozivamo ovo

class Person(ABC): # pravimo klasu osoba
    def __init__(self, name, surname,birth,adrees):
        self.name = name
        self.surname = surname
        self.birth = birth
        self.adrees = adrees
        super().__init__()

    @abstractmethod
    def __str__(self):
        pass

class Person(Employee): # pravimo klasu zaposlenih osoba
    broj_ljudi = 0

    def __init__(self, name, surname, birth, adrees,company,position,years,base_salary):
        super().__init__(name,surname,birth,adrees,company,position,years,base_salary)
        self.name = name
        self.surname = surname
        self.birth = birth
        self.adrees = adrees
        self.pompany = company
        self.position = position
        self.years = years
        self.base_salary = base_salary


        Employee.broj_ljudi += 1  # tada ce nam se broj ljudi koji su nezaposleni redom povecati za 1,kako ih dodavamo

    def __str__(self):
        return "Cao! Ja sam {0} {1}".format(self.name, self.surname)












x = Covjek("homo", "sapiens", "Tijana", "Sekaric", "1234")
x1 = Covjek("homo", "sapiens", "Stevan", "Sandi", "4321")

print(x)
print(x1)
print(Covjek.broj_ljudi