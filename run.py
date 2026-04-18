# Dunder __ builtins __, __init__
message = "PYHTON: Everything is object"
print(message)

result = type(message)
print("result:", result)

''' Init there are builtin tools
    (1) TYPES => int float str list dict
    (2)FUNCTION => print() len(uzunlikni o'lchaydi) input() type()  int( )
    (3) CONSTANTS => true false none 
    '''
print(dir(__builtins__))
