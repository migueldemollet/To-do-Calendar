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
        
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def get_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE id = ?;
        """, (id,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def get_by_name(self, name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE name = ?;
        """, (name,))
        
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def get_by_color(self, color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE color = ?;
        """, (color,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def get_custom(self, name, color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE name = ? AND color = ?;
        """, (name, color))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic
    
    def delete_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM tag WHERE id = ?;
        """, (id,))
        conn.commit()
        conn.close()
        return True

    def delete_by_name(self, name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM tag WHERE name = ?;
        """, (name,))
        conn.commit()
        conn.close()
        return True

    def delete_by_color(self, color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM tag WHERE color = ?;
        """, (color,))
        conn.commit()
        conn.close()
        return True


def convert_to_dict(rows):
    result = []
    for row in rows:
        d = {
            'name': row[1],
            'color': row[2]
        }
        result.append(d)
    return result