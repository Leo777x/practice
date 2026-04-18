print("==================")
# In JAVA, variable is name storage Location ma' man nomlanishi
# In PYHTON, variable is named reference - referensni nomlanishhi


count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"the count: {count} end type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("========  string  ==========")

# METHODS: upper(), lower(), title(), find(), replace()

course = "AI python fullstack"
result3 = type(course)
print(f"the sesult (1): {result3}")
result = course.title()
print(f"the sesult (2): {result}")
result = course.upper()
print(f"the sesult (3): {result}")

result = course.replace("fullstack", "MasterClass ")
print(f"the sesult (4): {result}")

print("========  bolean  ==========")

# Functions > type(), input(), bool(), int(), str()
y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric:{result}")

# TRUTHY vs FALSE value
# TRUTHY > true, 100, -100, "MIT" => bo'sh bolmagan strinlar va shular true hisob
# FALSE > falsy, 0, "", none => false qiymatlar hisoblanadi

test_false = "" or False or None or 0
print("the Falsy:", bool(test_false))

test_truthy = "MIT"
print("the truthy:", bool(test_truthy))
