'''🌟M-TASK (PYTHON)

Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham, 
orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.
MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;
'''
# 🌟 MASALANING YECHIMI:


def palindrom_check(word):
    return word == word[::-1]


# Test
print(palindrom_check("dad"))   # True
print(palindrom_check("son"))   # False


'''⭐️I-TASK (PYTHON)

Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
MASALAN: get_digits("m14i1t") return qiladi "141"
'''
# 🌟 MASALANING YECHIMI:


# def get_digits(text):
#     result = ""
#     for char in text:
#         if char.isdigit():
#             result += char

#     return result


# print(get_digits("m14i1t"))


'''⭐️G-TASK (PYTHON)

Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
'''

# 🌟 MASALANING YECHIMI:


# def get_highest_index(arr):
#     max_value = max(arr)
#     index = arr.index(max_value)  # shu qiymatning birinchi indexi
#     return index


# print(get_highest_index([5, 21, 12, 21, 8]))
