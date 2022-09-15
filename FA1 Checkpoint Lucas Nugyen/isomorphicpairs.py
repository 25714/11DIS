
def isomorphise(string1):
    num1 = 0
    num2 = 0
    currentchar = ""
    string3 = ""
    for index,char in enumerate(string1):
        currentchar = char
        for char in string1[index+1:len(string1)]:
            num1+=1
            if currentchar == char:
                num2 = num1
                num1 = 0
                break;
        if num2 > 0:
            num2 = f"+{num2}"
        string3 = f"{string3} {num2}"
        num1 = 0
        num2 = 0
    return string3
str1ng = "inn"
str2ng = "all"
if isomorphise(str1ng) == isomorphise(str2ng):
    print(True)








