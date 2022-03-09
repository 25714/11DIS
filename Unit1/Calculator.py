# Write a program that calculates the remainder of 10 divided by 3
# num1 = int(input("Enter the first number "))
# num2 = int(input("Enter the second number "))
# if (num1%num2) == 0:
#     print(True)
# else:
#     print(False)
# Write a rpogram that will print the following multi-line string:
# for i in range(3):
#     print("' '' '''")
# print(10-12.5*2)
#
# primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
#  101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
#  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
#  307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
#  401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
# endlist = []
# running = True
# starting = True
# index = 0
# while starting:
#     inputz = input("Input a number from 1-1000 ")
#     if inputz.isdigit():
#         if int(inputz) >=1 and int(inputz) <= 1000:
#             starting = False
#     else:
#         print("Not in bounds, please try again.")
#
# n = int(inputz)
# while running:
#     if n%primelist[index] == 0:
#         endlist.append(primelist[index])
#         n=n/primelist[index]
#         if n in primelist:
#             endlist.append(int(n))
#             print(f"The Prime Factors are: {endlist}")
#             running = False
#     else:
#         index +=1
#         if index >= len(primelist):
#             print(f"The Prime Factors are:[{inputz}""]")
#             running = False
# running = True
# while running:
#     thing = input("Type a set of digits to add. ")
#     num1 = 0
#     for i in range (0,len(thing)):
#         if thing[i].isdigit():
#             num1 += int(thing[i])
#     print(num1)
#     endinginput = input("Do you want to go again? (Y/N) ").lower()
#     if endinginput == "n":
#         running = False
# Divide the first number by the second number. If the remainder is 0, the smaller number is the GCD.
# If the remainder is not 0, replace the first number by the second number, and the second number by the remainder and reapeat from step 1.
#
# def GCD(num1,num2):
#     num3 = 1
#     while num3 != 0:
#         num3 = num1%num2
#         num1 = num2
#         num2 = num3
#     return(f"The GCD of the two numbers is {num1}")
# num1 = int(input("Please Input 1 number "))
# num2 = int(input("Please Input another number "))
# print(GCD(num1,num2))
# import random
# lives = 3
# a = random.randint(1,10)
# running = True
# asking = True
#
# while running:
#     while asking:
#         try:
#             b = int(input("Guess a number between 1 and 10 "))
#             asking = False
#         except:
#             print("Please input an Integer")
#     if b == a:
#         print("You win!")
#         running = False
#     if b > a:
#         print("Number too big!")
#         lives -= 1;
#     if b < a:
#         print("Number too small!")
#         lives -= 1;
#     if lives == 0:
#         print("You Lose Lmao")
#         print(f"The number was {a}")
#         running = False
#     asking = True
# Calculator.
def multiply(int1, int2):
    return int1 * int2


def add(int1, int2):
    return int1 + int2


def divide(int1, int2):
    if int2 == 0:
        return "Cant divide by 0"

    return int1 / int2


def subtract(int1, int2):
    return int1 - int2


def power(int1, int2):
    return int1 ** int2


def listcut(list1, list2):
    for e in range(0, len(list1)):
        try:
            list1.remove("$")
            list2.remove("$")
        except ValueError:
            pass


def calculator(equation):
    ostring = "*+-/^"
    equation = equation.replace(" ", "")
    nstring = ""
    nlist = []
    olist = []

    for char in equation:
        if char in ostring:
            if nstring == "" and char == "-":
                nstring += "-"
            else:
                try:
                    nlist.append(float(nstring))
                    olist.append(char)
                    nstring = ""
                except ValueError:
                    return(
                        "Equation Not in bounds. Use only *,+,/,-,^ and digits. Avoid using multiple operators at once, other than negative numbers.")
        if char.isdigit() or char == ".":
            nstring += char
    try:
        nlist.append(float(nstring))
    except ValueError:
        return(
            "Equation Not in bounds. Use only *,+,/,-,^ and digits. Avoid using multiple operators at once, other than negative numbers.")
    for i in range(0, len(olist)):
        if olist[i] == "^":
            nlist[i + 1] = power(nlist[i], nlist[i + 1])
            nlist[i] = "$"
            olist[i] = "$"
    listcut(nlist, olist)
    for i in range(0, len(olist)):
        if olist[i] == "*":
            nlist[i + 1] = multiply(nlist[i], nlist[i + 1])
            nlist[i] = "$"
            olist[i] = "$"
        if olist[i] == "/":
            nlist[i + 1] = divide(nlist[i], nlist[i + 1])
            if nlist[i+1] == "Cant divide by 0":
                return nlist[i+1]
            nlist[i] = "$"
            olist[i] = "$"
    listcut(nlist, olist)
    n = nlist[0]
    for i in range(0, len(olist)):
        if olist[i] == "+":
            # print(f"adding {n} and {nlist[i+1]}")
            n = add(n, nlist[i + 1])
        if olist[i] == "-":
            n = subtract(n, nlist[i + 1])
            # print(f"subtracting {n} and {nlist[i+1]}")
        if olist[i] == "^":
            n = power(n, nlist[i + 1])
    return f"{equation} = {n}"


running = True
while running:
    print(calculator(input("Input an equation to calculate ")))

    if input("Would you like to run the calculator again? (Y/N) ").lower() != "y":
        running = False

# How im going to do the brackets. If "()" Make a new string and that string gets immediate priority. and it will be epic, but idk how to do this for more importsnt
