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

