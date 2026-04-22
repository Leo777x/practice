'''CLASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE bu merso degan ma'noga ega
(3) POLIMORPHISM
'''

print("====== INHERITENCE ======== ")

'''
INHERITENCE bu merso degan ma'noga ega
INHERITENCE da PAREND va CHILD bor
INHERITENCE da > PAREND ozining CHILD classlariga ega bo'ladi

va PARENT o'zining public va protected holatdagi 
 prpertilarni pass qiladi,  state & method o'zining farzandlariga taqdim etadi

'''


class Animal:  # Parent class hisoblanadi
    # state
    description = "This class is parend for animal "
    # construction

    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice
    # method

    def make_voice(self):
        print(f"The animal can make voice {self.voice}")


class Dog(Animal):  # Child
    # state
    # construction
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you! ")

    def make_voice(self):
        print(f"The {self.name} says {self.sound}")

# agar INHERITENCE qonuniga ko'ra


class Cat(Animal):  # Child
    # state
    # construction
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child
    # state
    # construction
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "WOW-WOW", True)
cat = Cat("TOM", "Miao- Miao", True)
fish = Fish("NEMO", "Zz-zzzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-------------------")
dog.make_voice()
fish.make_voice()

print("------------")

print(Animal.description)
print("Dog:", Dog.description)

print(dog.voice, fish.voice)
print("status:", dog._status)

print("====== POLIMORPHISM ======== ")

'''
POLIMORPHISM nima degani? 
POLI - ko'p dagi
MORPHISM - shakl degani
ya'ni bir qancha narsalarnin shakli degani.
'''
print("-------")
# yuqorida hosil qilgan (fish)miz albatta Fish classidan  hosil bo'lgan Object hisoblanadi
# va (Fish) miz o'z navbatida Animal clasidan hosil bo'lgan hisoblanadi
# va ohirida hammasi Object degan classga child bo'lganini guvohi bo'lyamiz

a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)

result = a & b & c & d
print(f"the result: {result}")

# fish > animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object )
print("Data:", data1, data2)
