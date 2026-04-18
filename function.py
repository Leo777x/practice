'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametor vs Argument
(3) Keyword vs Default Argument
(4) Scope
'''
print("======== DEFINE (parametor) vs CALL (argument) ========")

# BUILD IN functions > print(), type(),
# FUNCTIONLAR> MA'LUM BIR MANTIQNI ISHGA TUSHIRIB BERUVCHI COD BLOC HISOBLANADI
# Function - reusable bloc of code deyiladi
# java da {} qavus bilan qilinsa pythonda.. indentation deyiladi


# Define
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is exuted")
    return f"Hi {b}"


# CALL
result1 = greet("LEO")
print("result1:", result1)

result2 = greeting("Justing")
print("result2:", result2)


print("======== Keyword vs Default Argument ========")

# define


def give_greet(name, age=27):
    print("give_greet is exucuted")
    return f"Hi {name}, you are {age}, years old!"


# Call qism
result3 = give_greet(name="LEO", age=26)  # Keyword argumenti

print("result3:", result3)

result4 = give_greet("LEO")
print("result4:", result4)
