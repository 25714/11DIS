#
# import jsonify
# from flask import Flask, render_template, request
# import requests
# import sqlite3, sys
#
# client_access_token = "uz8zgN2oyvnPex_z_3LRzCBAjtslU_snrKIwulUQdzdNK6l-kc6tcJakBgCcFRqy"
# search_term = "Taylor Swift"
# genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
# response = requests.get(genius_search_url)
# data = response.json()
# print(data)
# # for song in data['response']:
# #     print(song['result']['full_title'], song['result']['stats']['pageviews'])
import argon2
# from argon2 import PasswordHasher
# ph = PasswordHasher()
# hash = ph.hash("correct horse battery staple")
#
# print(ph.verify(hash, "correct horse battery staple"))

# from email.mime.text import MIMEText
# import smtplib
#
# from_email = "djfenners@outlook.com"
# from_password = "BigDJ100"
# outgoing_server = "smtp.office365.com"
# smtp_port = 587
#
# to_emails = ['lucasnguyenotlk@outlook.com','lucasnguyenotlk@outlook.com','lucasnguyenotlk@outlook.com','lucasnguyenotlk@outlook.com']
# names = ['name','name2','name3','name4']
# ids = [1,2,3,4]
# subject = "Hello!"
# for i, email in enumerate(to_emails):
#     message = f"""
#     Hey, {names[i]}
#     This is your ID {ids[i]}
#     """
#     msg = MIMEText(message,"html")
#     msg['Subject'] = subject
#     msg['To'] = email
#     msg['From'] = from_email
#
#     sending = smtplib.SMTP(outgoing_server,smtp_port)
#     sending.ehlo()
#     sending.starttls()
#     sending.login(from_email,from_password)
#     sending.send_message(msg)
# for i in to_email:
#     if names[to_email.index(i)] == 'Dinesh':
#         message = f'''
#         Congratulations! You live another day {names[to_email.index(i)]}...<br>
#
#         '''
#     else:
#         message = f'''
#         Congratulations! You live another day {names[to_email.index(i)]}...<br>
#
#         '''
#
#     msg = MIMEText(message, "html")
#     msg['Subject'] = subject
#     msg['To'] = i
#     msg['From'] = from_email
#     sending = smtplib.SMTP(outgoing_server, smtp_port)
#     sending.ehlo()
#     sending.starttls()
#     sending.login(from_email, from_password)
#     sending.send_message(msg)
#
#     print(f'Email sent to {names[to_email.index(i)]} completed.')
#
list = [('23khhseCLQqVMCIT1WMAns', 'SPS Music', '2023-06-05', 1), ('7ovUcF5uHTBRzUpB6ZOmvt', 'SPS Music', '2023-06-05', 1)]
