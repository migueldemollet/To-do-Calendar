import sqlite3

conn = sqlite3.connect('./DB/to_do_calendar.db')
c = conn.cursor()

#execute the following SQL to create the table user
c.execute('''DROP TABLE IF EXISTS user''')
c.execute(
'''
CREATE TABLE `user` (
  `id` integer PRIMARY KEY AUTOINCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) 
'''
)

#execute the following SQL to create the table tags 
c.execute('''DROP TABLE IF EXISTS tag''')

c.execute(
'''
CREATE TABLE `tag` (
  `id` integer PRIMARY KEY AUTOINCREMENT,
  `name` varchar(250) NOT NULL,
  `color` varchar(250) NOT NULL DEFAULT 'white',
  `id_user` int(10) NOT NULL,
  FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) 
'''
)

#execute the following SQL to create the table friends
c.execute('''DROP TABLE IF EXISTS friends''')

c.execute(
'''
CREATE TABLE `friends` (
  `id` integer PRIMARY KEY AUTOINCREMENT,
  `id_user_1` int(10) NOT NULL,
  `id_user_2` int(10) NOT NULL,
  `state` int(2) NOT NULL DEFAULT 0,
  FOREIGN KEY (`id_user_1`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`id_user_2`) REFERENCES `user` (`id`) ON DELETE CASCADE
)
'''
)

#execute the following SQL to create the table task
c.execute('''DROP TABLE IF EXISTS task''')
c.execute(
'''
CREATE TABLE `task` (
  `id` integer PRIMARY KEY AUTOINCREMENT,
  `name` varchar(250) NOT NULL,
  `description` text NOT NULL DEFAULT '',
  `state` int(2) NOT NULL DEFAULT 0,
  `date` varchar(150) NOT NULL,
  `priority` int(2) NOT NULL DEFAULT 0,
  `color` varchar(150) NOT NULL DEFAULT 'white',
  `id_tag` int(10) NOT NULL,
  `id_user` int(10) NOT NULL,
  FOREIGN KEY (`id_tag`) REFERENCES `tag` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE CASCADE
)
'''
)

#execute the following SQL to create the table user_task
c.execute('''DROP TABLE IF EXISTS user_task''')
c.execute(
'''
CREATE TABLE `user_task` (
  `id` integer PRIMARY KEY AUTOINCREMENT,
  `user_id` int(10) NOT NULL,
  `task_id` int(10) NOT NULL,
  `role` int(2) NOT NULL,
  FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`task_id`) REFERENCES `task` (`id`) ON DELETE CASCADE
) 
'''
)

conn.commit()
conn.close()
