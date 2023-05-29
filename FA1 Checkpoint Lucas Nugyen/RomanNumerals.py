import requests, json, sqlite3
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
# def RomanNumerals(number):
#     values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#     numerals = ""
#     for i in range(0,13):
#         while number >= values[i]:
#             number = number - values[i]
#             numerals += roman[i]
#     return(numerals)
#
#
# number = int(input("Please input a number between 1-3999. "))
# if 1 <= number <= 3999:
#     print(RomanNumerals(number))
# # else:
# #     print("Error")
#
#
# URL = f'https://theaudiodb.com/api/v1/json/523532/searchtrack.php?s=&t=cardigan'
# response = requests.get(URL)
# data = response.json()
# # print(data)
# json.loads('["hello", "yo"]')
# print( json.loads('["hello", "yo"]'))
# dictionary = {'one': 'asd', 'two' : 'asda'}
# values = []
# for key in dictionary:
#     values.append(dictionary[key])
#
#
#
# print(f"INSERT INTO {'albums'} VALUES ({', '.join(values)})")
# # conn
# dictionary = {'user_id': 3, 'song_id': 3}
# conn = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA2App\ndjdatabase.db')
# values = []
# for key in dictionary:
#     if dictionary[key] == None:
#         values.append("None")
#     else:
#         values.append(dictionary[key])
# conn.execute(f"INSERT INTO songs_fave VALUES ({('?,'*len(values))[0:(len(values)*2)-1]})", (values))
# # conn.execute(f"INSERT INTO songs_fave VALUES ({', '.join(values)})"), (values)
# conn.commit()
# conn.close()
data = [17, (2, 3, '2005-12-12', 'Epilogue', 2), 0, (4, 3, '2005-12-12', 'Prologue', 1)]
i = 0;
for dat in data:
    i += 1;

