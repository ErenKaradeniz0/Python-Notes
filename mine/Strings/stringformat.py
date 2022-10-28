name = 'Limon'
surname = 'Kuş'
age = 1
print('My name is {} {}'.format(name, surname)) # My name is Çınar Turan
print('My name is {1} {0}'.format(name, surname))  # My name is Turan Çınar
print('My name is {s} {n}'.format(n=name, s=surname))  # My name is Turan Çınar
print("My name is {} {} and I'm {} years old.".format(name, surname, age))
print("My name is {} {} and I'm {} years old.".format(name, name, name)) # My name is Çınar Çınar Çınar
print("My name is {0} {0} and I'm {0} years old.".format(name)) # My name is Çınar Çınar Çınar
print(f"My name is {name} {surname} and I'm {age} years old.")
