import sqlite3

class TaskModel:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task;
        """)
        
        return convert_to_dict(cursor.fetchall())

    def get_by_name(self, name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE name = ?;
        """, (name,))
        
        return convert_to_dict(cursor.fetchall())

    def get_by_status(self, status):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE status = ?;
        """, (status,))
        conn.close()

        return convert_to_dict(cursor.fetchall())
    
    def get_by_tag(self, tag):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE tag = ?;
        """, (tag,))
        conn.close()

        return convert_to_dict(cursor.fetchall())

    def get_by_date(self, date):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE date = ?;
        """, (date,))
        conn.close()

        return convert_to_dict(cursor.fetchall())

    def get_by_color(self, color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE color = ?;
        """, (color,))
        conn.close()

        return convert_to_dict(cursor.fetchall())
    
    def get_by_priority(self, priority):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE priority = ?;
        """, (priority,))
        conn.close()

        return convert_to_dict(cursor.fetchall())

    def get_custom(self, name, status, tag, date, color, priority):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE name = ? AND status = ? AND tag = ? AND date = ? AND color = ? AND priority = ?;
        """, (name, status, tag, date, color, priority))
        conn.close()
        
        return convert_to_dict(cursor.fetchall())
    


def convert_to_dict(self, rows):
        result = []
        for row in rows:
            d = {
                'name': row[0],
                'status': row[1],
                'tag': row[2],
                'date': row[3],
                'color': row[4],
                'priority': row[5]
            }
            result.append(d)
        return result
    