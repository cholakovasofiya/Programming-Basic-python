number = int(input())
bonus = 0

if number <= 100:
    bonus = 5
elif number > 100 and number <= 1000:
    bonus = number*20/100
elif number > 1000:
    bonus = number*10/100

if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2

number += bonus
print(bonus)
print(number)










