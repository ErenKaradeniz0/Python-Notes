sehirler = ['ankara', 'izmir']


def change(n):
    n[0] = 'istanbul'
    print(n)


change(sehirler[:])
print(sehirler)


def add(*params):
    # print(type(params)) <class 'tuple'>
    sum = 0
    for n in params:
        sum = sum + n
    return sum


print(add(10, 20, 50))
print(add(10, 20, 30))
print(add(10, 20, 30, 50, 60, 10, 20))


def displayUser(**args):
    # print(type(args)) <class 'dict'>
    for key, value in args.items():
        print('{} is {}'.format(key, value))


print()
displayUser(name='Çınar', age=2, city='istanbul')
print()
displayUser(name='Ada', age=12, city='kocaeli', phone='123132')
print()
displayUser(name='Yiğit', age=14, city='ankara', phone='123132', email='yigit@gmail.com')



def myfunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


myfunc(10, 20, 30, 40, 50, 60, 70, key1='value 1', key2='value 2')