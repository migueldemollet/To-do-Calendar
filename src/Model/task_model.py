import sqlite3

class TaskModel:
    def __init__(self, db_name):
        self.db_name = db_name

    def add_task(self, task):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO task (name, status, tag, date, color, priority) VALUES (?, ?, ?, ?, ?, ?);
        """, (task.name, task.status, task.tag, task.date, task.color, task.priority))
        conn.commit()
        conn.close()

    def get_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task;
        """)

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def get_by_name(self, name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE name = ?;
        """, (name,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def get_by_status(self, status):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE status = ?;
        """, (status,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic
    
    def get_by_tag(self, tag):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE tag = ?;
        """, (tag,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def get_by_date(self, date):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE date = ?;
        """, (date,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def get_by_color(self, color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE color = ?;
        """, (color,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic
    
    def get_by_priority(self, priority):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE priority = ?;
        """, (priority,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def get_custom(self, name, status, tag, date, color, priority):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE name = ? AND status = ? AND tag = ? AND date = ? AND color = ? AND priority = ?;
        """, (name, status, tag, date, color, priority))
        
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def delete_by_name(self, name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM task WHERE name = ?;
        """, (name,))
        conn.commit()
        conn.close()
        return True
    


def convert_to_dict(rows):
    result = []
    for row in rows:
        d = {
            'name': row[1],
            'status': row[2],
            'tag': row[3],
            'date': row[4],
            'color': row[5],
            'priority': row[6]
        }
        result.append(d)
    return result
    