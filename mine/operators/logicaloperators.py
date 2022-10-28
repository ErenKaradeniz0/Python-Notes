# x = int(input("bir sayı giriniz : "))
# result = (x > 0) and ((x % 2) == 0)
# print(f"{x} : çift pozitif : {result}")

vize1 = int(input("vize1 notunu giriniz : "))
vize2 = int(input("vize2 notunu giriniz : "))
final = int(input("final notunu giriniz : "))
ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
result = (ortalama >= 50 and final > 50) or final >= 70
print(f"ortalamanız {ortalama} geçti mi {result}")


name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)

zayif = (index >= 0) and (index<=18.4)
normal = (index>18.4) and (index<=24.9)
kilolu = (index>24.9) and (index<=29.9)
obez = (index>=29.9) and (index<=34.9)

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')