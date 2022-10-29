import sqlite3

class TagModel:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def add(self, tag):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO tag (name, color) VALUES (?, ?);
        """, (tag.name, tag.color))
        conn.commit()
        conn.close()
        return True

    def get_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag;
        """)
        
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def delete_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM tag;
        """)
        conn.commit()
        conn.close()
        return True

    #-------------------------Id-------------------------------

    def get_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE id = ?;
        """, (id,))

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

    #-------------------------Name-------------------------------

    def get_by_name(self, name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE name = ?;
        """, (name,))
        
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def change_name(self, name, new_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE tag SET name = ? WHERE name = ?;
        """, (new_name, name))
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

    #-------------------------Color-------------------------------

    def get_by_color(self, color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE color = ?;
        """, (color,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def change_color(self, name, new_color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE tag SET color = ? WHERE name = ?;
        """, (new_color, name))
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