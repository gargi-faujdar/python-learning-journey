import random
target=random.randint(1,100)

while True:
    guess=int(input("enter your number: "))
    if guess==target:
        print("YAY!! you guessed the correct number")
        break
    if guess<target:
        print("oops! you guessed the smaller number")
    else:
        print("sorry!! the number guessed is too big")


print("----GAME OVER-----")