#2 Länder

#1a På Island bor det 383726 invånare och i Danmark 5961249.
# Skapa objekt för länderna. (Data från januari 2024. Avrunda befolkningen.)

#1b Lägg till en metod med namnet "print_info".
# Om man anropar den för Sverige-objektet ska den skriva ut:
# "I Sverige bor det 10.5 miljoner invånare". Funktionen ska använda sina egenskaper,
# så att den fungerar för de andra länderna också.

#1c Lägg till landets area som en egenskap till klassen. Använd en parameter till konstruktorn,
# alltså __init__ metoden. Ge arean ett default värde på None så att man inte måste ange arean
# när man skapar ett landsobjekt.
#Exempel på default värde för en vanlig funktion:
# y har default värde 10
#def exempel(x, y=10):
#    print(x + y)

#exempel(2)  # skriver ut 12

#1d Ändra i metoden "print_info" så att den skriver ut arean också, men bara om arean inte är None.

#1e Skapa en ny metod med namnet "add_language". Den ska lägga till ett av landets officiella språk.
# (Sverige har bara ett, men Finland har två språk (svenska och finska) och Schweiz har fyra.)
# För att kunna spara ett varierande antal behöver du använda en lista.

#1f Ändra i "print_info" så att den skriver ut alla officiella språk, på en ny rad.


class Country:
    def __init__(self, name, pop, area = None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__official_languages = []

    def print_info(self):
        print(f"I {self.__name} bor det {self.__population} miljoner invånare")
        if self.__area is not None:
            print(f"Landets area är: {self.__area} km2")
        if len(self.__official_languages) != 0:
            print(f"Landets officiella spräk är: {self.__official_languages} ")

    def add_language(self, lng):
        self.__official_languages.append(lng)
        print(f"{lng} tillkom som officiellt språk för {self.__name}")




se = Country("Sverige", 10.5, 450295)
se.add_language("svenska")
se.print_info()

no = Country("Norge", 5.5)
no.print_info()

isl = Country("Island", 0.4, 103000)
isl.print_info()
dk = Country("Danmark", 6)
dk.print_info()

fi = Country("Finland", 5.6)
fi.add_language("svenska")
fi.add_language("finska")
fi.print_info()







