def RomanNumerals(number):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numerals = ""
    for i in range(0,13):
        while number >= values[i]:
            number = number - values[i]
            numerals += roman[i]
    return(numerals)

