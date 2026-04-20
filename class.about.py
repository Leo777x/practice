'''CLASS
(1) What is class
(2) ordinary vs static properties
(3) special / magic methods
'''
print("======= What is class =======")

# class lar object yasash uchun hismat qiladigon shablon hisoblanadi
# sturcture: conistructor, state, method


class Person():
    # state
    message = "class state property"
    # conistructor

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says:  How do you do!")

    def say_age(self):
        print(f"{self.name} says i am {self.age}! ")

    @classmethod
    def explain(cls):
        print("static method property exucuted!")


person1 = Person("Justin", 25)
person2 = Person("Leo", 26)
person3 = Person("Martin", 36)


print("person1.name:", person1.name)

person1.introduce()
person2.say_age()

print("======= ordinary vs static properties =======")

# static satate
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()

print("======= special / magic methods =======")

# Python's most common special methods are below:
# __init__, __new__, __str__, __call__, __getitem__, __eq__, __len__...


class car():
    # state
    description = "This class makes cars"
    # conistructor

    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year
    # method

    def start_engine(self):
        print(f"the{self.name} started engine!")

    def stop_engine(self):
        print(f"the{self.name} stopped engine!")

    def __str__(self):
        return f"the car.name: {self.name} was produced in {self.year} year! "

    def __call__(self):
        print("Object called as function")
        return True


my_car = car("Ferarri", 2026)
my_car.start_engine()
my_car.stop_engine()

print("-----")
your_car = car("Toyota", 2020)
print(your_car)

response = your_car()  # Call
print("response:", response) 