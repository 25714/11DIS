import jsonify
from flask import Flask, render_template, request
import requests
import sqlite3, sys
def search_albums(artist_name):
    API_KEY = '523532'
    URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/searchalbum.php?s={artist_name}'
    response = requests.get(URL)
    data = response.json()
    albums = data['album']
    return albums

def search_track(album_id):
    API_KEY = '523532'
    URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/track.php?m={album_id}'
    response = requests.get(URL)
    data = response.json()
    track = data['track']
    return track
def search_track_id(track_id):
    API_KEY = '523532'
    URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/track.php?h={track_id}'
    response = requests.get(URL)
    data = response.json()
    track = data['track']
    return track

def search_artist(artist_name, type):
    API_KEY = '523532'
    if type == "name":
        query = "search.php?s"
    if type == "id":
        query = "artist.php?i"
    URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/{query}={artist_name}'
    response = requests.get(URL)
    data = response.json()
    return data
def save_albums_to_db(artist_name, album_id, albums):
        conn = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA2App\ndjdatabase.db')
        conn.execute("INSERT INTO albums VALUES (?,?,?)", (album_id, artist_name,  albums))
        conn.commit()
        conn.close()

def dictionary_into_db(dictionary, tablename):
    conn = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA2App\ndjdatabase.db')
    values = []
    for key in dictionary:
        if dictionary[key] == None:
            values.append("None")
        else:
            values.append(dictionary[key])
    conn.execute(f"INSERT INTO {tablename} VALUES ({('?,'*len(values))[0:(len(values)*2)-1]})", (values))
    # conn.execute(f"INSERT INTO songs_fave VALUES ({', '.join(values)})"), (values)
    conn.commit()
    conn.close()

    # except:
    # return(f"INSERT INTO {tablename} VALUES ({', '.join(values)})")


def spotify_search_track(string,offset):

    url = "https://api.spotify.com/v1/search/"
    querystring = {"q": string,"type":"track","offset":offset, "limit":"20","numberOfTopResults":"5"}
    key = "BQA9qmXaOspJH7RuA9mbGRFLL_HXzMMHrff3CirZ_GOSWad3dmLFkESMkkmCZ9EsgBw9B6egRYm_uDldANqKg79h_Y3inBRB5ie6aBCiUBojsdZUT2Y"
    headers = {
        "Authorization": f"Bearer {key}",}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data
    # for point in data['tracks']['items']:
    #     print(point['name'],point['explicit'])
    # print(data)
