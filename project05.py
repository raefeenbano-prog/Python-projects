import random
while True:
    print("\n🎲 rolling the dice....")
    dice = random.randint(1,6)
    print("you got:",dice)
    choice = input("roll again ?(yes/no):").lower()
    if choice != "yes":
        print("Thanks for playing!")
        break
    