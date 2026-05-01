'''G-TASK (PYTHON)

Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
'''

#🌟 MASALANING YECHIMI:

def get_highest_index(arr):
    max_value = max(arr)        
    index = arr.index(max_value)  # shu qiymatning birinchi indexi
    return index

print(get_highest_index([5, 21, 12, 21, 8]))
