import jsonify
from flask import Flask, render_template, request
import requests
import sqlite3, sys
from email.mime.text import MIMEText
import smtplib
def dictionary_into_db(dictionary, tablename):
    conn = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA3App\ndjdatabase.db')
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
    key = "BQCVnU-rMrBTi4H2saDAT5ZIwYzVO2vvtjeJmCLBxAgcBfk0RRmHJ09ZtJbd_a2v0dUqme7F8asvwkZoeDr72PVuyukq3olpE93cwj65EKvkLhQszzI"
    headers = {
        "Authorization": f"Bearer {key}",}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data
    # for point in data['tracks']['items']:
    #     print(point['name'],point['explicit'])3w
    # print(data)

def spotify_search_tracks(ids):
    url = 'https://api.spotify.com/v1/tracks/'
    params = {"ids": ids}
    key = "BQCVnU-rMrBTi4H2saDAT5ZIwYzVO2vvtjeJmCLBxAgcBfk0RRmHJ09ZtJbd_a2v0dUqme7F8asvwkZoeDr72PVuyukq3olpE93cwj65EKvkLhQszzI"
    headers = {
        "Authorization": f"Bearer {key}",}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data
    # for point in data['tracks']['items']:
    #     print(point['name'],point['explicit'])
    # print(data)

def send_email(to_emails, subject, text):
    from_email = "djfenners@outlook.com"
    from_password = "BigDJ100"
    outgoing_server = "smtp.office365.com"
    smtp_port = 587
    # to_emails = ['lucasnguyenotlk@outlook.com','lucasnguyenotlk@outlook.com','lucasnguyenotlk@outlook.com','lucasnguyenotlk@outlook.com']
    # names = ['name','name2','name3','name4']
    # ids = [1,2,3,4]
    # subject = "Hello!"
    for email in to_emails:
        message = f"""
        Hey, {email[1]} 
        {text}
        This is your ID {email[2]}
        """

        msg = MIMEText(message,"html")
        msg['Subject'] = subject
        msg['To'] = email[0]
        msg['From'] = from_email

        sending = smtplib.SMTP(outgoing_server,smtp_port)
        sending.ehlo()
        sending.starttls()
        sending.login(from_email,from_password)
        sending.send_message(msg)
