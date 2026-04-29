'''Packages & debugging
(1) Python Packages & Core Packages
(2) Package Manager & External Package
(3) Debugging
'''
from PIL import image
import turtle
print("======= Python Packages & Core Packages ========")

''' 
Pythoda package larimiz / Modul ham  deb atalar ekan 
va Pythoda package larimiz 3 hil turda bo'lar ekan 
(1) Core
(2) File
(3) External 
'''
# Core Packages >  https://docs.python.org/3/liberary


# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(3)
# t.circle(200)

# turtle.done()

print("--------------")

my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with

with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE")

print("======= Package Manager & External Package ========")
# package manager (pip)
# Pythonda > pip pipenv
# NodeJs > npm yarm
# PHP > Composeer
# macos brew
# External Package > https://pypi.org/

with Image.open("material/IMG_1215.JPG") as img_obj:
     resized_img = img_obj.resize((200, 200))
     resized_img.show()
     resized_img.save("material/sample.png")

