import sqlite3

conn = sqlite3.connect('temp.db')
c = conn.cursor()
c.execute("""Select * from MOVIE""")
res = c.fetchall()
movie = res[0]
aid = res[0][5]
actorname = ""
c.execute(""" SELECT FIRST_NAME,LAST_NAME FROM ACTOR WHERE AID=(?);""", (aid,))
print(c.fetchall()[0][0])

mid=res[0][0]
c.execute(""" SELECT GENRE FROM GENRE WHERE MID=(?);""", (mid,))
temp = c.fetchall()
genrefull = temp[0][0]
for i in range(1, len(temp)):
    genrefull+=", "
    genrefull+=temp[i][0]
print(genrefull)
