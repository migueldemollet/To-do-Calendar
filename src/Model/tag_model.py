import sqlite3

class TagModel:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def get_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag;
        """)
        
        return convert_to_dict(cursor.fetchall())

    def get_by_name(self, name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE name = ?;
        """, (name,))
        
        return convert_to_dict(cursor.fetchall())

    def get_by_color(self, color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE color = ?;
        """, (color,))
        conn.close()

        return convert_to_dict(cursor.fetchall())

    def get_custom(self, name, color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE name = ? AND color = ?;
        """, (name, color))
        conn.close()

        return convert_to_dict(cursor.fetchall())

def convert_to_dict(rows):
    result = []
    for row in rows:
        d = {
            'name': row[0],
            'color': row[1]
        }
        result.append(d)
    return result