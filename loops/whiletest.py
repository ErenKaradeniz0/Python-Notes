sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
x = 0
while x < len(sayilar):
    print(sayilar[x])
    x += 1

x = int(input("başlangıç indexini girin : "))
y = int(input("bitiş indexini girin : "))

while x < y:
    if(x%2==1):
        print(x)
    x += 1

# num = 100
# while num >= 0:
#     print(num)
#     num -= 1

