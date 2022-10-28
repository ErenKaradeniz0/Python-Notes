# def write(word, number):
#     while number > 0:
#         print(word)
#         number -= 1
#
# def write2(word, number):
#     for a in range(number):
#         print(word)
#
# write("selam", 3)
# write2("selam", 3)
#
# def convertlist(*args):
#     list=[]
#     for param in args:
#         list.append(param)
#     return list
# print(convertlist(1,2,55,5151,515,4))


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def findprime(number1, number2):
    for sayi in range(number1, number2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)


number1 = int(input('number 1:'))
number2 = int(input('number 2:'))

findprime(number1, number2)

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.
#
#
# def tamBolenleriBul(sayi):
#     tamBolenler = []
#
#     for i in range(1, sayi+1):
#         if sayi % i == 0:
#             tamBolenler.append(i)
#
#     return tamBolenler
#
#
# print(tamBolenleriBul(40))
