'''ARRAY & SET
(1) Array
(2) Set
(3) Specific operator with set
'''
from array import array
print("========== Array ===========")

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


print("========== Set ===========")

'''
set mantig'i unique colection deyiladi ya'ni:
takrorlanmaydigan elementlar to'plami desak
😎 mubolag'a bo'lmaymiz
va yana setlarimizda ketma - ketlik tushunchasi bo'lmaydi
va set mantig'ida doim gulli qavus hosil bo'ladi
'''
new_numbrs = array("i", [1, 5, 4, 5, 7, 8, 7, 41])
numbs_set = set(new_numbrs)  # shu orqali pass qildik

print(f"the numbs_set: {numbs_set} and type {type(numbs_set)}")

numbs_set.add(200)  # 200 raqamini ohiriga qo'shsak
print("numbs_set:🧐(1)", numbs_set)


# set bu unique to'plamligi sabab bir sonni qayta kiritib bo'lmaydi
numbs_set.add(7)
print("numbs_set:(2)", numbs_set)


print("========== Specific operator with set : maxsus ope..  ===========")
# |, &, -, ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union da har ikkala toplamdagi qiymatlarni alohida setga joylab beradi
# va bir-xilda kelgan qiymatlarni bittasini qabul qilib qolganini olmaydi.
print("result1:", result1)

result2 = a & b  # and belgisi bu bizga intersection ni hosil qilib beradi
# intersection degani ikkala toplamdagi bir-xil son yoki ma'lumotni olib beradi
print("result2:", result2)

# diference  degani: birinchi to‘plamda bor, lekin ikkinchisida yo‘q elementlar
result3 = a - b
print("result3:", result3)

# semetric diference da ikkita to'plamda qatnashmagan sonlarni olib beradi.
result4 = a ^ b
print("result4:", result4)
