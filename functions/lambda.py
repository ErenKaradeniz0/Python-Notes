def square(num): return num ** 2
squarelambda = lambda num: num ** 2

numbers = [1, 3, 5, 9, 10, 4]

result = list(map(lambda num: num ** 2, numbers))
result2 = list(map(square, numbers))
result3 = squarelambda(3)
print(result, result2, result3)

for item in map(square, numbers):
    print(item)


def check_even(num): return num % 2 == 0


check_even_lambda = lambda num: num % 2 == 0

result = list(filter(check_even, numbers))
result1 = list(filter(lambda num: num % 2 == 0, numbers))
result2 = list(filter(check_even_lambda, numbers))

result3 = check_even_lambda(numbers[2])

print(result, result1, result2, result3)
