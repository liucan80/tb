import urllib.request

import sqlite3 as lite
import sys

response=urllib.request.urlopen('https://www.baidu.com/img/bd_logo1.png')
html=response.read()
tempdile=open('c:/tes1.png','wb')
tempdile.write(html)
tempdile.close()
# !/usr/bin/python
# -*- coding: utf-8 -*-
def readImage():
    try:
        fin = open("c:/tes1.png", "rb")
        img = fin.read()
        return img
    except IOError:

        print("2")
        sys.exit(1)

    finally:

        if fin:
            fin.close()


con = lite.connect('c:/test1.db')
cur = con.cursor()
cur.execute("CREATE TABLE Images(Id INTEGER PRIMARY KEY, Data BLOB)")
data = readImage()
binary = lite.Binary(data)
cur.execute("INSERT INTO Images(Data) VALUES (?)", (binary,))
con.commit()
