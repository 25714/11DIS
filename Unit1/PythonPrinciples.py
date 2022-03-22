def capital_indexes(estring):
    caplist = []
    for i in range(len(estring)):
        if estring[i].isupper():
            caplist.append(i)
    return(caplist)
def mid(string):
    if len(string)%2 != 0:
        return(string[int(len(string)/2)])
    else:
        return("")
def online_count(dictionary):
    count = 0
    for online in dictionary:
        if dictionary[online] == "online":
            count+= 1
    return(count)
import random
def random_number():
    return random.randint(1,101)
def only_ints(num1, num2):
    if type(num1) == int and type(num2) == int:
        return True
    else:
        return False
def double_letters(estring):
    for i  in range(len(estring)):
        if estring[i] == estring[i-1]:
            return True
    return False
def add_dots(estring):
    estring = ".".join(estring)
    return(estring)
def remove_dots(estring):
    string2 = ""
    for char in estring:
        if char == ".":
            pass
        else:
            string2 += char
    return string2
def count(estring):
    newlist = []
    newlist = estring.split("-")
    return(len(newlist))
def is_anagram(string1,string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False
def flatten(lists):
    newlist = []
    for element in lists:
        newlist += element
    return newlist
def largest_difference(thelist):
    intH = thelist[1]
    intL = thelist[1]
    for element in thelist:
        if element > intH:
            intH = element
    for element in thelist:
        if element < intL:
            intL = element
    return(intH-intL)
def div_3(num):
    if num%3 == 0:
        return True
    return False
def get_row_col(string):
    cols = ["A", "B", "C"]
    rows = ["1", "2", "3"]
    row = 0
    col = 0
    for i in range(len(cols)):
        if string[0] == cols[i]:
def palindrome(estring):
    if estring == estring[::-1]:
        return(True)
    return False
def up_down(num1):
    return(num1-1,num1+1)
def consecutive_zeros(string):
    n = 0
    nmax = 0
    for i in string:
        if i == "0":
            n += 1
        else:
            n = 0
        if n > nmax:
            nmax = n
    return nmax
def all_equal(lists):
    for i in range(len(lists)):
        if lists[i] != lists[i-1] :
            return False
    return True
def triple_and(bool1,bool2,bool3):
    if bool1 == True and bool2 == True and bool3 == True:
        return True
    return False
def convert(thelist):
    return [str(x) for x in thelist]
def zap(a,b):
    newlist = []
    for i in range(len(a)):
        newlist.append((a[i],b[i]))
    return newlist
def validate(string):
    if "def" not in string:
        return("missing def")
    if ":" not in string:
        return("missing :")
    if "(" not in string:
        return("missing paren")
    if ")" not in string:
        return("missing paren")
    if "(.)".replace(".","") in string:
        return("missing param")
    if "    " not in string:
        return("missing indent")
    if "validate" not in string:
        return("wrong name")
    if "return" not in string:
        return("missing return")
    else:
        return True
def list_xor(n,list1,list2):
    if n in list1 and n not in list2:
        return True
    if n not in list1 and n in list2:
        return True
    return False
def param_count(*argv):
    return len(argv)
def format_number(intz):
    intz = str(intz)[::-1]
    string = ""
    for i in range(len(intz)):
        string += intz[i]
        if (i+1)%3 == 0:
            string+=","
    return string[::-1].strip(",")
