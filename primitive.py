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
