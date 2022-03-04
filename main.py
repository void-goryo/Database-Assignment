

import sqlite3

conn = sqlite3.connect('test.db')   #create database
fPath = 'C:\\Users\\Gabe\\Desktop\\Database-Assignment'
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


with conn:
    cur = conn.cursor() #control through commands

    cur.execute('CREATE TABLE IF NOT EXISTS tbl_assignment(\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            file TEXT)')

    conn.commit #save
conn.close

with conn:
    cur = conn.cursor()

    for i in fileList:  #starts 'i' and goes through tuple
        if '.txt' in i: #if .txt is in a string
             cur.execute('INSERT INTO tbl_assignment(file) VALUES (?)',(i,))
                 #'i' is a tuple and it fills in '?'. single tuples need a ',' afterwards
    conn.commit
conn.close

with conn:
    cur = conn.cursor()
    cur.execute('SELECT id, file FROM tbl_assignment')  #select the file and id column from the assignment table
    varFile = cur.fetchall()
    for file in varFile:
        print(file)
