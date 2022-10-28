# program that sums all odd numbers and detects all even numbers between 0-100
x = 0
result = 0

while x <= 100:
    x += 1

    if x % 2 == 0:
        print(f"  even number detected the number is : {x}")
        continue

    result += x

print(f'sum is : {result}')
