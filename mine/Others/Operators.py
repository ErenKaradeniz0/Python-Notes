# print(bool("Hello"))
# print(bool(15))
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool({}))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

myFunction()

print(2**3)
print(9//2)

x = ["apple", "banana"]

print("banana" in x)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y