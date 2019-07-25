import sqlite3
from datetime import datetime
import dateutil
from dateutil.relativedelta import relativedelta


conn = sqlite3.connect('temp8.db')

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

insert_director(1, datetime.date(datetime(1958,9,10,0,0,0,0)), 'Chris', 'Columbus')
insert_actor(1, datetime.date(datetime(1989,6,23,0,0,0,0)), 'Daniel', 'Redcliff')


c.execute("""INSERT INTO MOVIE VALUES(1, 2001, "HARRY POTTER AND THE SORCERER'S STONE", "An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.", 1, 1, 7.6);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(1, "Adventure");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(1, "Family");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(1, "Fantasy");""")
conn.commit()



insert_director(2, datetime.date(datetime(1938,11,4,0,0,0,0)), 'Joe', 'Pytka')
insert_actor(2, datetime.date(datetime(1963,2,17,0,0,0,0)), 'Micheal', 'Jordan')


c.execute("""INSERT INTO MOVIE VALUES(2, 1996, "SPACE JAM", "In a desperate attempt to win a basketball match and earn their freedom, the Looney Tunes seek the aid of retired basketball champion, Michael Jordan.", 2, 2, 6.8);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(2, "Comedy");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(2, "Animation");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(2, "Adventure");""")
conn.commit()

insert_director(3, datetime.date(datetime(1958,12,9,0,0,0,0)), 'Raja', 'Gosnell')
insert_actor(3, datetime.date(datetime(1970,1,24,0,0,0,0)), 'Matthew', 'Lillard')


c.execute("""INSERT INTO MOVIE VALUES(3, 2002, "SCOOBY DOO", "After an acrimonious break up, the Mystery Inc. gang are individually brought to an island resort to investigate strange goings on.", 3, 3, 5.0);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(3, "Comedy");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(3, "Family");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(3, "Adventure");""")
conn.commit()

insert_director(4, datetime.date(datetime(1958,7,25,0,0,0,0)), 'Tim', 'Burton')
insert_actor(4, datetime.date(datetime(1951,9,5,0,0,0,0)), 'Micheal', 'Keaton')


c.execute("""INSERT INTO MOVIE VALUES(4, 1992, "BATMAN RETURNS", "When a corrupt businessman and the grotesque Penguin plot to take control of Gotham City, only Batman can stop them, while the Catwoman has her own agenda.", 4, 4, 7.0);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(4, "Action");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(4, "Crime");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(4, "Fantasy");""")
conn.commit()


insert_director(5, datetime.date(datetime(1964,12,7,0,0,0,0)), 'Karey', ' Kirkpatrick')
insert_actor(5, datetime.date(datetime(1980,4,26,0,0,0,0)), 'Channing', 'Tatum')


c.execute("""INSERT INTO MOVIE VALUES(5, 2018, "SMALLFOOT", "A Yeti is convinced that the elusive creatures known as humans really do exist.", 5, 5, 6.7);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(5, "Comedy");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(5, "Animation");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(5, "Adventure");""")
conn.commit()


insert_director(6, datetime.date(datetime(1965,5,21,0,0,0,0)), 'Lana', 'Wachowski')
insert_actor(6, datetime.date(datetime(1985,3,13,0,0,0,0)), 'Emile', 'Hirsch')


c.execute("""INSERT INTO MOVIE VALUES(6, 2008, "SPEED RACER", "A young driver, Speed Racer, aspires to be champion of the racing world with the help of his family and his high-tech Mach 5 automobile.", 6, 6, 6.0);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(6, "Comedy");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(6, "Action");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(6, "Adventure");""")
conn.commit()



insert_director(7, datetime.date(datetime(1945,3,3,0,0,0,0)), 'George', 'Miller')
insert_actor(7, datetime.date(datetime(1981,1,28,0,0,0,0)), 'Elijah', 'Wood')


c.execute("""INSERT INTO MOVIE VALUES(7, 2006, "HAPPY FEET", "Into the world of the Emperor Penguins, who find their soul mates through song, a penguin is born who cannot sing. But he can tap dance something fierce!", 7, 7, 6.5);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(7, "Comedy");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(7, "Animation");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(7, "Adventure");""")
conn.commit()


insert_director(8, datetime.date(datetime(1947,9,21,0,0,0,0)), 'Nick', 'Castle')
insert_actor(8, datetime.date(datetime(1920,10,1,0,0,0,0)), 'Walter', 'Matthou')


c.execute("""INSERT INTO MOVIE VALUES(8, 1993, "DENNIS THE MENACE", "When his parents have to go out of town, Dennis stays with Mr. and Mrs. Wilson. The little menace is driving Mr. Wilson crazy, but Dennis is just trying to be helpful. Even to the thief who's arrived in town.", 8, 8, 5.6);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(8, "Comedy");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(8, "Family");""")
conn.commit()





insert_director(9, datetime.date(datetime(1976,3,19,0,0,0,0)), 'Nicholas', 'Stoller')
insert_actor(9, datetime.date(datetime(1978,8,18,0,0,0,0)), 'Andy', 'Samberg')


c.execute("""INSERT INTO MOVIE VALUES(9, 2016, "STORKS", "Storks have moved on from delivering babies to packages. But when an order for a baby appears, the best delivery stork must scramble to fix the error by delivering the baby.", 8, 8, 6.8);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(9, "Comedy");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(9, "Animation");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(9, "Adventure");""")
conn.commit()





insert_director(10, datetime.date(datetime(1943,5,20,0,0,0,0)), 'Simon', 'Wincer')
insert_actor(10, datetime.date(datetime(1963,10,14,0,0,0,0)), 'Lori', 'Petty')


c.execute("""INSERT INTO MOVIE VALUES(10, 1993, "FREE WILLY", "When a boy learns that a beloved killer whale is to be killed by the aquarium owners, the boy risks everything to free the whale.", 10, 10, 5.9);""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(10, "Family");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(10, "Drama");""")
conn.commit()
c.execute("""INSERT INTO GENRE VALUES(10, "Adventure");""")
conn.commit()



insert_director(11, datetime.date(datetime(1958,9,10,0,0,0,0)), 'Rakesh', 'Roshan')
insert_actor(11, datetime.date(datetime(1989,6,23,0,0,0,0)), 'Hritik', 'Roshan')



c.execute("""select sql from sqlite_master where type = 'table';""")
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


                

