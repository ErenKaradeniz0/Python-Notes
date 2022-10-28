items = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))

i = 0

while(i<adet):
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    items.append({
        'name': name,
        'price': price
    })
    i += 1

for item in items:
    print(f'ürün adı: {item["name"]} ürün fiyatı: {item["price"]}')