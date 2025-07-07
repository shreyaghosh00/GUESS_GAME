import random
import math

lower = int(input("Enter Lower Limit:- "))
upper = int(input("Enter Upper Limit:- "))
x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")

count = 0
flag = False
while count < total_chances:
    count += 1
    guess = int(input("Guess a number:- "))


    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        flag = True
        break
    elif x > guess:
        print("Your Guess too small!")
    elif x < guess:
        print("Your Guess too high!")

if not flag:
    print("\nThe number is %d" % x)
    print("\tGood Play, Better Luck Next time!")


