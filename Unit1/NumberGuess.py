import random
a = random.randint(1,10)
lives = 3
for i in range (lives):
    b = None
    while b == None:
        try:
            b = int(input("Guess a number between 1 and 10 "))
        except:
            print("Please input an Integer")
    if b == a:
        print("You win!")
        break;
    if b > a:
        print("Number too big!")
    if b < a:
        print("Number too small!")
if b != a:
    print("You Lose Lmao")
    print(f"The number was {a}")
