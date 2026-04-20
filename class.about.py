'''CLASS
(1) What is class
(2) ordinary vs static properties
(3) special methods
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
