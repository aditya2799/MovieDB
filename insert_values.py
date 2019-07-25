import sqlite3
from datetime import datetime
import dateutil
from dateutil.relativedelta import relativedelta


conn = sqlite3.connect('temp.db')

print("OK")

c = conn.cursor()



c.execute(""" CREATE TABLE DIRECTOR (
                DID INTEGER PRIMARY KEY ,
                DOB DATE,
                AGE INT,
                FIRST_NAME TEXT,
                LAST_NAME TEXT);""")

c.execute(""" CREATE TABLE ACTOR (
                AID INTEGER PRIMARY KEY ,
                DOB DATE,
                AGE INT,
                FIRST_NAME TEXT,
                LAST_NAME TEXT);""")

c.execute(""" CREATE TABLE MOVIE (
                MID INTEGER PRIMARY KEY ,
                YOR INT,
                NAME TEXT,
                DESCRIPTION TEXT,
                DID INT,
                AID INT,
                RATING REAL,
                FOREIGN KEY (DID) REFERENCES DIRECTOR(DID),
                FOREIGN KEY (AID) REFERENCES ACTOR(AID)
                );""")

c.execute(""" CREATE TABLE GENRE (
                MID INTEGER ,
                GENRE TEXT,
                FOREIGN KEY (MID) REFERENCES MOVIE(MID)
                );""")




def insert_director(did, dob, fn, ln):
    age= relativedelta(datetime.now(), dob).years
    c.execute(""" INSERT INTO DIRECTOR VALUES(?, ?, ?, ?, ?);""",(did, dob, age, fn, ln))
    conn.commit()

def insert_actor(aid, dob, fn, ln):
    age= relativedelta(datetime.now(), dob).years
    c.execute(""" INSERT INTO aCTOR VALUES(?, ?, ?, ?, ?);""",(aid, dob, age, fn, ln))
    conn.commit()

insert_director(1, datetime.date(datetime(1983,5,20,0,0,0,0)), 'Utsav', 'Pro')
insert_actor(1, datetime.date(datetime(1983,5,20,0,0,0,0)), 'Utsav', 'Pro')


c.execute("""INSERT INTO MOVIE VALUES(1, 2001, "HARRY POTTER AND THE SORCERER'S STONE", "An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.", 1, 1, 7.6);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(1, "Adventure");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(1, "Family");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(1, "Fantasy");""")
conn.commit()











c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")

print(c.fetchall())

c.execute("Select * from director;")
print(c.fetchall())

c.execute("Select * from actor;")
print(c.fetchall())

c.execute("Select * from MOVIE;")
print(c.fetchall())

c.execute("Select * from GENRE;")
print(c.fetchall())


                
