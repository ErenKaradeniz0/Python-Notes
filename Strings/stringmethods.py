message = "Hello there. My name ıs Star gırl"

print("_______________________________________________________________________________________")
message = message.upper()
print(message)
message = message.lower()
print(message)
print("_______________________________________________________________________________________")

message = message.title()
print(message)
message = message.capitalize()
print(message)
print("_______________________________________________________________________________________")

message = message.strip()
print(message)
print("_______________________________________________________________________________________")

message = message.split()
print(message)
message = " ".join(message)
print(message)
print("_______________________________________________________________________________________")

index = message.find("star")
print(index)
isfound1 = message.startswith("H")
isfound2 = message.endswith("l")
print(isfound1, isfound2)
print("_______________________________________________________________________________________")

message = message.replace("girl", "boy")
print(message)
message = message.replace("ı", "i").replace("", "*")
print(message)


print("_______________________________________________________________________________________")

message = "Hello there. My name is Star boy"

message = message.center(87, '*')
print(message)
print("_______________________________________________________________________________________")