sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
toplam = 0
for sayi in sayilar:
    toplam += sayi
print('toplam:', toplam)

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
for s in sehirler:
    if (len(s) <= 5):
        print(s)

urunler = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'}
]
toplam = 0
for urun in urunler:
   fiyat = int(urun['price'])
   toplam += fiyat
print('toplma ürün fiyatı: ', toplam)

for urun in urunler:
    if(int(urun["price"])<=5000):
        print(urun["name"])
