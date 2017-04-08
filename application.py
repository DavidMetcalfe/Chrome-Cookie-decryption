import os.path
from shutil import copy
import sqlite3
from datetime import datetime

import win32crypt

'''
Extract and decrypt cookie information from
Chrome cookie databases on Windows.

Initial code inspiration from Jordan Wright <jordan-wright.github.io>

March 9 2017 '''


def getCookieDB():
    userhome = os.path.expanduser('~')
    destination = os.path.dirname(os.path.realpath(__file__))

    filePath = os.path.normpath(os.path.join(
                    userhome, 'AppData\\Local\\Google\\Chrome'
                    '\\User Data\\Default\\cookies'))

    copy(filePath, destination)


getCookieDB()

# Connect to the Database
conn = sqlite3.connect('cookies')
cursor = conn.cursor()

# Get the results
cursor.execute('''
    SELECT name, 
    encrypted_value, 
    host_key, 
    path, 
    secure, 
    httponly, 
    creation_utc, 
    expires_utc 
    FROM cookies 
    ORDER BY host_key
    ''')

with open('export.txt', 'w') as f:

    for result in cursor.fetchall():

        f.write("Name: {}\n".format(result[0]))
        f.write("Content: {}\n".format(
            win32crypt.CryptUnprotectData(result[1])[1].decode()))
        f.write("Domain: {}\n".format(result[2]))
        f.write("Path: {}\n".format(result[3]))
        if result[4] == 1:
            f.write("Send for: Secure connections only\n")
        else:
            f.write("Send for: Any kind of connection\n")

        if result[5] == 1:
            f.write("Accessible to script: Yes\n")
        else:
            f.write("Accessible to script: No (HttpOnly)\n")

        # To do: Convert UTC to naive datetime at minimum.
        f.write("Created: {}\n".format(result[6]))
        f.write("Expires: {}\n".format(result[7]))
        f.write("\n\n")
