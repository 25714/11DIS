# Isomorphic pairs algorithm.
# Begin Program IsomorphicPairs(string1)
# Initialise num1 as 0
# Initialise num2 as 0
# Initialise currentchar as empty string
# Initialise index as 0
# initialise string3 as empty string
# for char in string1:
#     currentchar = char
#     for char in string1(from the index+1th letter):
#         num1 = num1+1
#         if currentchar == char:
#             num2 = num1
#             num1 = 0
#             break
#         endif
#     Interate index (+1)
#     endfor
#         if num2 > 0:
#             num2 = +{num2} as string
#         endif
#             string3 = ({string1} {num2}) as string
#             num1 = 0
#             num2 = 0
#         endfor
#     endfor
#     return string3
# if word1 length != word2 length:
#     Word1 and Word2 are not isomorphic.
# endif
# if IsomorphicPairs(word1) == IsomorphiPairs(word2):
#     Word1 and word2 are isomorphic
# else:
#     Word1 and Word2 are not isomorphic
# endif

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


