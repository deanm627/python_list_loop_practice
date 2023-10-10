import random

def result():
    if (user_num < 1 or user_num > 10):
        print("YOU'RE OUT OF RANGE!!")
        return

    if (user_num == magic_number):
        print("ARE YOU A MIND READER!?!?!")
    else:
        print("That's incorrect, try again")

user_num = int(input("Guess a number between 1-10: "))

magic_number = random.randint(1, 10)
print("Magic number is: %s"%(magic_number))

result()