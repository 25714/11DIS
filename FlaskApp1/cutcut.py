# Def RPSLS
# gamelist = “2,4”, ”3,0”, ”1,3”, ”4,0”, ”2,1”
# guess = input from player (into int)
# a = random number
# for index option in enumerate(gamelist):
# 	if option == b:
# 		b = index
# if b in gamelist[a]:
# 	return “loss”
# elif a in gamelist[b]:
# 	return “win”
# else:
# 	return “Tie”
# endif
import random
def cutgame(b):
    mydict = {
        "0": "2,4", "1": "3,0", "2": "1,3", "3": "4,0", "4": "2,1"
    }
    gamelist = ["Paper","Scissors","Rock","Lizard","Spock"]

    a = random.randint(0,4)
    for index,option in enumerate(gamelist):
        if option.lower() == b.lower():
            b = f"{index}"
    try:
        low = int(b)
        if b in (mydict[f"{a}"]):
            return ["You Lose! :(", gamelist[a]]
        elif f"{a}" in (mydict[f"{b}"]):
            return ["You Win! :)", gamelist[a]]
        else:
            return ["You Tied", gamelist[a]]
    except TypeError:
        return "Bad Input"
