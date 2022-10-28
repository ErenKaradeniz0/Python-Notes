message = " Hello World "
message = message.lstrip()
print(message)

message = " Hello World "
message = message.rstrip()
print(message)

message = " Hello World "
message = message.strip()
print(message)

website = "https://www.btkakademi.gov.tr/"
result=website.strip("hpst://.wgovtr")
print(result)

name="eren"
print(name.count('e'))
print(name.find("ren"))
print(name.isalpha())
print("elma1".isdigit())

result="content".center(50)
print(result)
result="content".center(50,'*')
print(result)
result="content".ljust(50,'*')
print(result)
result="content".rjust(50,'*')
print(result)

