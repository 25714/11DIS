import requests

url = "https://accounts.spotify.com/api/token"

headers = {
	"Content-Type": "application/x-www-form-urlencoded"
}
client_id = "8aa92861253e4f0bb14af10f68a7c49c"
client_secret = "84d242ac3e164a3a956904fa4f4c93b2"
data = {
	"grant_type": "client_credentials",
	"client_id": client_id,
	"client_secret": client_secret
}

response = requests.post(url, headers=headers, data=data)

print(response.json())
#
#
# search = input("Search Track ")
# url = "https://api.spotify.com/v1/search/"
# querystring = {"q": search,"type":"track","offset":"0","limit":"20","numberOfTopResults":"5"}
# key = "BQAOF60v95UNaRZMeIYVZvQdtamf2BXLLikKDVYc4rfIXOKT2PQ4d3TTsQ4XMw5YB2AaVpJbnPLHvShrSUPkMl6_M2bWN8mW7Jw5SkM2FFnIaVqwZgM"
# headers = {
# 	"Authorization": f"Bearer {key}",
# }
# #
# response = requests.get(url, headers=headers, params=querystring)
# data = response.json()
# for point in data['tracks']['items']:
# 	print(point['name'],point['explicit'], point['album']['images'][0]['url'])
# print(data)
#
# # for point in data['artists']['items']:
# 	print(point)
#
# for point in data['artists']['items']:
# 	print(point['name'])
#
#
# print(data)
#
