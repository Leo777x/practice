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
