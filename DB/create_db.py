import sqlite3

conn = sqlite3.connect('./DB/to_do_calendar_test.db')
c = conn.cursor()

#remove tables
c.execute("DROP TABLE IF EXISTS task")
c.execute("DROP TABLE IF EXISTS tag")
c.execute("DROP TABLE IF EXISTS user")
c.execute("DROP TABLE IF EXISTS friend")

c.execute('''CREATE TABLE task (id integer primary key, name text unique, status integer, tag integer, date text, color text, priority integer)''')


#create table tag with columns id, name unique, color
c.execute('''CREATE TABLE tag (id integer primary key, name text unique, color text)''')

#create table user with columns id, username unique, email unique, password
c.execute('''CREATE TABLE user (id integer primary key, username text unique, email text unique, password text)''')

#create table friend with columns id, id_user1, id_user2, confirmed
c.execute('''CREATE TABLE friend (id integer primary key, id_user1 integer, id_user2 integer, confirmed integer)''')

#insert data into table tag
c.execute("INSERT INTO tag VALUES (1, 'tag1', 'red')")
c.execute("INSERT INTO tag VALUES (2, 'tag2', 'blue')")
#insert data into table task
c.execute("INSERT INTO task VALUES (1, 'task1', 0, 1, '01/01/2022', 'red', 1)")
c.execute("INSERT INTO task VALUES (2, 'task2', 1, 2, '01/02/2022', 'blue', 2)")

#insert data into table user
c.execute("INSERT INTO user VALUES (1, 'user1', 'user1@tdcalendar.com', 'be3a7f14702be45fd3157db6144ca5bc')")
c.execute("INSERT INTO user VALUES (2, 'user2', 'user2@tdcalendar.com', 'f998bdf7077a317b289a99b98a5f44d6')")
#insert data into table friend
c.execute("INSERT INTO friend VALUES (1, 1, 2, 0)")

conn.commit()
conn.close()
