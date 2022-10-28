length = int(input("enter length of array  : "))
numbers = [0] * length
i = 0
while i < len(numbers):
    x = int(input(f"enter {i}. element of array with length {length} : "))
    numbers[i] = x
    i += 1
numbers.sort()
print(numbers)


