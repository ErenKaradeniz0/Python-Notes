import random

change = int(input("enter number of change : "))
counter = 0
randomnumber = (random.randint(1, 100))
score = 100
diff = int(score / change)
min, max = 0, 100
guess = int(input(f"enter your guess interval at {min} - {max}  : "))

while change > 0:
    change -= 1
    counter += 1
    if guess == randomnumber:
        print(f"you gueessed right at {counter}. guees and your score is : {score}")
        break
    elif guess < randomnumber:
        if min < guess:
            min = guess
        print("your guess is too low")
        print(f"{change} change left")
        guess = int((input(f"enter your guess at interval {min} - {max} :")))
    else:
        if max > guess:
            max = guess
        print("your guess is too high")
        print(f"{change} change left")
        guess = int((input(f"enter your guess at interval {min} - {max}  :")))
    score -= diff
    if change == 0:
        print("you lost")
