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

print("======== set and dictionariy comp==========")
print("------------")

# bu... "set" orqali tayorlagan comprehensionimiz
numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}
print("set_numbs:", set_numbs)

# bu esa "dictionary" orqali tayorlagan comprehensionimiz
# biz comprehension orqali "dict_people"  objectimiz ya'ni Jyson object deyiladi
dict_people = {person[0]: person[1] for person in people}  # b version
print("dict_people:", dict_people)

dict_people2 = {person[0]: person[1]
                for person in people if person[1] > 20}  # b version


print("dict_people2:", dict_people2)
 