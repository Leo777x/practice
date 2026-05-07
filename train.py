'''⭐️I-TASK (PYTHON)

Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
MASALAN: get_digits("m14i1t") return qiladi "141"
'''
# 🌟 MASALANING YECHIMI:


def get_digits(text):
    result = ""
    for char in text:
        if char.isdigit():
            result += char

    return result


print(get_digits("m14i1t"))


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
