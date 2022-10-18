import sqlite3

conn = sqlite3.connect('./DB/to_do_calendar_test.db')
c = conn.cursor()

#remove tables
c.execute("DROP TABLE IF EXISTS task")
c.execute("DROP TABLE IF EXISTS tag")

c.execute('''CREATE TABLE task (id integer primary key, name text unique, status integer, tag integer, date text, color text, priority integer)''')


#create table tag with columns id, name unique, color
c.execute('''CREATE TABLE tag (id integer primary key, name text unique, color text)''')

#insert data into table tag
c.execute("INSERT INTO tag VALUES (1, 'tag1', 'red')")
c.execute("INSERT INTO tag VALUES (2, 'tag2', 'blue')")
#insert data into table task
c.execute("INSERT INTO task VALUES (1, 'task1', 0, 1, '01/01/2022', 'red', 1)")
c.execute("INSERT INTO task VALUES (2, 'task2', 0, 2, '01/02/2022', 'blue', 2)")

conn.commit()
conn.close()
