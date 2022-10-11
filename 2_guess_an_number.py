import random

set_top_random = int(input("Enter top of number? "))
random_number = random.randint(1, set_top_random)
guesess = 0

while True:
    guesess += 1
    answer = int(input("Enter guess number: "))
    if answer == random_number:
        print("Correct!")
        break
    elif answer >= random_number:
        print("Your number above the random number!")
    else:
        print("Your number below the random number!")

print(f"You guesess with {guesess} time")
