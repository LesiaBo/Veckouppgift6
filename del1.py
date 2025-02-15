#1 Läsa och förstå kod - diskutera i grupp
#Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?


#1 Vad gör följande kod?
class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)

#-> koden skapar 2 insatser x och y av klass SafeStorage,
# placerar värde "Anakonda" och "Boaorm", efter detta returnerar dem värdena och skriver dem ut.
#---------------------------------------------------------

#2a Vad gör följande kod? Fixa eventuella fel.
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(shelf):
        super().make_noise()
        print("Mjau!")

def sound_off(animal):
    animal.make_noise()

c = Cat()
d = Dog()
#h = Rooster()-> instead:
h = Animal()
#sound_off([c, d, h]) -> instead:
c.make_noise()
d.make_noise()
h.make_noise()

#->Detta djur har vi inget ljud för.
#->Mjau
#->Voff
#->Detta djur har vi inget ljud för.

#-------------------------------------------------------
class Guldfisk(Animal):
    def swimming_posibility(self):
        print("Yes, I can swim")

e = Guldfisk()
e.make_noise()
e.swimming_posibility()




