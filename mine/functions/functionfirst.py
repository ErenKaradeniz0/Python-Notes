def sayHello(user):
    print(f"hello {user}")


def sayHello2(user):
    return (f"hello {user}")


sayHello("ali")
print(sayHello2("ali"))


def total(num1, num2):
    return num1 + num2


print(total(1, 5))


def calculateage(birthyear):
    return 2022 - birthyear


print(calculateage(2002))


def emelilikyılı(birthyear, name):
    age = calculateage(birthyear)
    emeklilik = 65 - age
    return emeklilik


print(f"{emelilikyılı(1974, 'ali')} yıl kaldı")
