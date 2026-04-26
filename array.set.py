'''ARRAY & SET
(1) Array
(2) Set
(3) Specific operator with set
'''
from array import array
print("==========  ===========")

'''
Asosan biz arrayni o'rniga list dan foydalanamiz. 
lekin 🥴 ma'lumotimiz juda katta hajimga ega bo'lsa pythoda, ARRAY lardan foydalanamiz
'''
numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers1:", numbers)
numbers.append(100)  # ohiridan 100 qo'yadi
numbers.insert(0, 14)  # boshidan 14 ni qo'yib beradi
print("numbers2:", numbers)

numbers.remove(5)  # bu yerda remove 5 raqamini o'chirib tashlayabdi
numbers.pop()  # pop methodi ohiridagi 100 ni olib tashayabdi
print("numbers3:", numbers)

# bu yerda dell methodi 0 dan 2 gacha bo'lgan sonni o'chirib yubordi
del numbers[0:2]

print("numbers4:", numbers)
 