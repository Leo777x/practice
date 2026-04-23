'''Tuple
(1) What is tuple: typle vs list
(2) Unpacking arguments
(3) zip
'''
print("======= What is tuple: typle vs list===========")
# Java/PHP/NodeJS array => python list, array

# literal
numbs = [3, 5, 1, 2]


# constructor
letters = list("Hello World!")
# print(letters)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits", fruits)

fruits[2] = "melon"
print("after fruits", fruits)


# Biz hechqachon tuple ni qiymatini o'zgartira olmaymiz
animals = ("dog", "cat", "fish", "lemon")

print(animals[0])
# manabu yerda o'zgartirib bo'lmaydi sababi tuple bo'lganligi
# animals[0] = "bird"


print("======= Unpacking arguments argumenlarni yoyish ===========")

groups = ["MIT", "FLEXY", "DEVEX", "MG"]

(x, y, *z) = groups

print(f"the x: {x} and y: {y}")
print("z:", z)  # list


# *args > tuple
def calculate(*args):
    print("*args:", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
print("-----------")
calculate(0, 2, 300)
print("-----------")
calculate(5, 7)


