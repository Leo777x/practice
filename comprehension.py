'''Comprehension
(1) What Comprehension & list comp
(2) set and dictionariy comp.
'''
print("======== What Comprehension & list comp ==========")

'''Comprehension nima?
Comprehension.. bu boshqa tillardagi spreat aperatori amali pythonda Comprehension da qilinar ekan
Comprehension larni umumiy qolipi mavjud ular:>
a: maxsus (*) belgi so'ng  iterable objectini qo'yishimiz mumkin
b: <expression> for item in iterable
c: <expression> for item in iterable <condition>
'''
# list comp

numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version
print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("--------------")
people = [("Robert", 20), ("Steve", 19), ("Josep", 25)]
list_people = [person[0] for person in people]  # b version
print("list_people", list_people)

print("------------")
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]
# carning har-bitta qiymatini biz cars orqali chaqirib olyabmiz 
list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars", list_cars)
