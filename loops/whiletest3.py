items = []
length = int(input("enter number of item : "))
i = 0
while i < length:
    name = input("enter product name : ")
    price = int(input("enter product price : "))
    items.append({"name": name, "price": price})
    i += 1
for item in items:
    print(f'product name is : {item["name"]} product price is : {item["price"]}')
