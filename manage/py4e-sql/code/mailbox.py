# import database library
import sqlite3

# establish connection with server
conn = sqlite3.connect('orgdb.sqlite')
cursor = conn.cursor()

# create table
cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# feed data to table
fname = 'D:\GitHub_Projects\py4e-sql\dataset\mbox.txt'
fhand = open(fname)
for line in fhand:
    if line.startswith('From: '):
        pieces = line.split()
        org = pieces[1].split('@')
        org = org[1]
        cursor.execute('SELECT count FROM Counts WHERE org = ?', (org,))
        row = cursor.fetchone()
        if row is None:
            cursor.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
        else:
            cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    else:
        continue
    
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 20'

for row in cursor.execute(sqlstr):
    print(row[0],'\t:', row[1])

conn.commit()
cursor.close()
