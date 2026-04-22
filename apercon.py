'''OPERATORS & CONDITIONS
(1)operators
(2)conditions
(3)logical operators
'''
print("======= operators ========")
# + - >= < <= * /  // % += **

a = 19
b = 5
result = a // b
left = a % b

print(f"the result {result} end left: {left}")


# a = a + 100
a += 100
print("a:", a)

print("b*b:", b**2)  # b ning  kvadratini olib  beryabdi
print("b*b*b:", b**3)  # b ning  kubini olib  beryabdi uch marttaga ko'paytirdi

print("="*7)

c = dict(name="LEO", age=26)
d = dict(name="LEO", age=26)
e = c
print("c==d:", c == d)  # only value
print(id(c), id(d), id(e))

print("c is d:", c is d)
print("c is d:", c is e)
 