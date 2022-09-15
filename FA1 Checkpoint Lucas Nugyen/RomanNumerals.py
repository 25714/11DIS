# Begin Program RomanNumerals
# 	Store values 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
# 	Store roman: "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
# 	Initialize numerals to empty string
# 	ask user for number between 1 and 3999
# 	If number in correct range
# 		For i = 0 to 12
# 			while number >= values[i]
# 				number = number – values[i]
# 				append corresponding roman to numerals
# 			End while
# 			increment i
# 		End for
# 	Else:
# 		Display error
# 	End If
# End Program RomanNumerals
def RomanNumerals(number):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numerals = ""
    for i in range(0,13):
        while number >= values[i]:
            number = number - values[i]
            numerals += roman[i]
    return(numerals)


number = int(input("Please input a number between 1-3999. "))
if 1 <= number <= 3999:
    print(RomanNumerals(number))
else:
    print("Error")
