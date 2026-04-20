'''OBJECTS
(1) What is object
(2) Iterable objects & RANGE
(3) DICTIONARY
(4) Eror handling system
'''

import array  # package / module
import math  # package
from math import ceil
print("===== What is object =====")
# and object has state and method properties
# objectlarimiz o'zining state va methodlariga ega bo'lgan data type xisoblanadi
# Evreythin is object in Python Paytondahamma narsa object

print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))


# numberni math objectining  ceil methodiga argument sifatida pass qilamiz ya'ni CALL qilyabmiz
# va ceil mthodining define qismi math packegida hisoblanadi.
result1 = math.ceil(97.7)
print('result1:', result1)

result2 = ceil(98.7)
print("result2:", result2) 
