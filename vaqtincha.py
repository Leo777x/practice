'''list 
(1) workin with lists
(2) list methods
(3) lambda function
(4) enumarate, map and filter
'''
print("========== workin with lists ===========")

''' 
Paythondagi list ushunchasi boshqa tillardagi "Array" lar bilan bir-xil
yoziladi ya'ni: Java / PHP / NodeJes da:  array ni => (list) data type orqali yozar ekanmiz. 
(list)larimizni hosil qilishimizda ikki xil usuli bor ekan bu:
1 - Kvadrat qavs ([]) bilan
2 - list() konstruktori orqali
'''
# BIZ UNDAN OLDIN
# literal usul
person = {"name": "Justin", "age": 26}  # dictionary key bilan ishlaydi
print("person:", person)

# tuplelarimiz asosan (,) larimiz bian yoziladi:
people = ("Andrew", "John", "Michael")  # tuple
print("people:", people)

# 1 - Kvadrat qavs ([]) bilan yoziladigon listimiz
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list

for team in groups:
    print(f"the team: {team}")


# Constructor usulidagi listlarimiz qanday yoziladi? :


letters = list("Hello World!")
print(f"the letters: {letters} and size: {len(letters)}")

'''
Bu yerda list("Hello World!") orqali biz list classining constructorini chaqiryapmiz.
Natijada "Hello World!" stringidagi har bir belgidan iborat yangi 
list object yaratiladi va u letters o‘zgaruvchisiga saqlanadi.
'''

print("----------")
# .           0.       1.       2.       3
fruits = ["appe", "orange", "lemon", "kivi"]

a = fruits[0]
# bu qanday ishlaydi yarim interval deyiladi ya'ni 0 ning o'zi kiradi lekin 2 ning o'zi kirmaydi
b = fruits[0:2]
# 0 da joylashgan appe 1 da joylashgan orange ni olib beradi lekin 2 da joylashgan "le" ol bermaydi

c = fruits[::3]
print("a:", a)
print("b:", b)
print("c:", c)
'''
::2 → har 2 index sakraydi
::3 → har 3 index sakraydi
::4 → har 4 index sakraydi
::5 → har 5 index sakraydi
qanday bo'ladi?
2 → bittasini ol, bittasini tashla
3 → bittasini ol, 2 tasini tashla
4 → bittasini ol, 3 tasini tashla
5 → bittasini ol, 4 tasini tashla
soddaroq tushunamiz:
'''

alphabit = ["a", "b", "c", "d", "e", "f", "g", "h"]

d = alphabit[::3]
m = alphabit[::-1]
print("d:", d)
print("m:", m)
