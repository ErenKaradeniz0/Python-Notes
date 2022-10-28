import random

"""
This is a comment
written in
more than just one line
"""
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
# print(type(x))
# print(type(y))
# print(type(z))

a = 4
A = "Sally"
#A will not overwrite a

# x, y, z = "Orange", "Banana", "Cherry"
# print(x, y, z)
# print()
# x = y = z = "Orange"
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
# print()
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x,y,z)
# print(x + y + z)

#data types

x = 1j	#Complex numbers are written with a "j" as the imaginary part:
x = ["apple", "banana", "cherry"]   #list
x = ("apple", "banana", "cherry")   #tuple
x = {"apple", "banana", "cherry"}   #set
x = frozenset({"apple", "banana", "cherry"})    #frozen set
x = range(6) #range
x = {"name" : "John", "age" : 36} #dict
x = b"Hello" #bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) #memoryview
x = None #none type


#global variable

x = "awesome"

def myFunction():
    global x
    x = "fantastic" #local variable
    print("Python is " + x)

# myFunction()

# print("Python is " + x)

#random

# print(random.randrange(1, 10))

#casting

y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
w = float("4.2") # w will be 4.2

y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'



#Strings

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

a = "Hello, World!"
# print(len(a))
# print(a[1])

# for x in a:
#   print(x)
#in keyword

txt = "The best things in life are free!"
# print("free" in txt)

# if "free" in txt:
#   print("Yes, 'free' is present.")
txt = "The best things in life are free!"

# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")


#slicing
b = "Hello, World!"
# print(b[2:5])
# print(b[:5])
# print(b[2:])
# print(b[-5:-2])  #Use negative indexes to start the slice from the end of the string:

#modify
a = "   Hello, World!  "
# print(a.upper())
# print(a.lower())
# print(a.strip()) # returns "Hello, World!"
# print(a.replace("H", "J"))
# print(a.split(",")) # returns ['Hello', ' World!'] The split() method returns a list where the text between the specified separator becomes the list items.

#format strings

quantity = 3
item_number = 567
price = 49.95
my_order = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(my_order.format(quantity, item_number, price))

# print("\t apple\n orange \" cherry \" bread") 
# print("apple".center)

#string methods
a="my strings    "
print(a.count("s"))
print(a.replace("m","a"))
print(a.index("s"))
print(a.strip())
