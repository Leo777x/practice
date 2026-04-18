print("======== Numbers ==========")
# In JAVA, variable is name storage Location ma' man nomlanishi
# In PYHTON, variable is named reference - referensni nomlanishhi


count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"the count: {count} end type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("======== String  ==========")
# eng ko'p ishlatiladigon methodlar: upper(), lower(), title(), find(), replace()

course = "AI Python Fullstack"
result = type(course)
print(f"the result (1): {result}")
result = course.title()
print(f"the result (2): {result}")
result = course.replace("Fullstack", "MasterClass")
print(f"the result (3): {result}")
print(course)

print("======== Boolean  ==========")

# Functions => type(), input(), bool(), int(), str()

y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"The input is numeric {result}")

# TRUTHY vs FALSE value
# TRUTHY : true, 100, -100, "bo'sh bo'lmagan stringlar"
# FALSE : false, 0, "", none
test_false = "" or False or None or 0
print("the FALSE:", bool(test_false))

test_truthy = "" "MIT"
print("the FALSE:", bool(test_truthy))
