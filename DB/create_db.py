import sqlite3

conn = sqlite3.connect('./DB/to_do_calendar_test.db')
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

#insert data into table user
c.execute(
  '''
  INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
  (1, 'user1', 'user1@tdcalendar.com', '5e06b84ac4f276aa03afc04fd1e82856'),
  (2, 'user2', 'user2@tdcalendar.com', 'd6f85014ab40ab641c6b801818c4b681'),
  (3, 'user3', 'user3@tdcalendar.com', 'cc0e14efb403fc5d6a07fbe1dc278e84')
  '''
)

#insert data into table tags
c.execute(
  '''
  INSERT INTO `tag` (`id`, `name`, `color`, `id_user`) VALUES
  (1, 'tag1', 'bisque', 1),
  (2, 'tag2', 'DarkOliveGreen1', 1),
  (3, 'tag3', 'LightPink2', 2)
  '''
)
c.execute(
  '''
    INSERT INTO `task` (`id`, `name`, `description`, `state`, `date`, `priority`, `color`, `id_tag`, `id_user`) VALUES
    (1, 'task1', 'description1description1description1description1description1description1description1des cription1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1description1', 0, '05/11/2022', 0, 'red', 1, 1),
    (2, 'task2', 'description2', 1, '06/11/2022', 1, 'blue', 2, 1),
    (3, 'task3', 'description3', 1, '05/12/2022', 2, 'green', 3, 1),
    (4, 'task4', 'ESTO', 0, '06/11/2022', 1, 'blue', 2, 1),
    (5, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (6, 'task6', 'UN', 0, '06/11/2022', 1, 'blue', 2, 1),
    (7, 'task4', 'ESTO', 0, '06/11/2022', 1, 'blue', 2, 1),
    (8, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (9, 'task6', 'UN', 0, '06/11/2022', 1, 'blue', 2, 1),
    (10, 'task4', 'ESTO', 0, '06/11/2022', 1, 'blue', 2, 1),
    (11, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),

    (111, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 1, 1),
    (112, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 1, 1),
    (113, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (114, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 3, 1),
    (115, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (116, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (117, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (118, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (119, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (120, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    
    (1110, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (1120, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (1130, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (1140, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (1150, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (1160, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (1170, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (1180, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (1190, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),
    (1200, 'task5', 'ES', 0, '06/11/2022', 1, 'blue', 2, 1),

    (12, 'task6', 'UN', 0, '06/11/2022', 1, 'blue', 2, 1),
    (13, 'task7', 'PROGRAMON', 0, '06/11/2022', 1, 'blue', 2, 1)
    '''
)

#insert data into table friend
#c.execute("INSERT INTO friend VALUES (1, 1, 2, 0)")

conn.commit()
conn.close()
