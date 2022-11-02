import sqlite3

class TagModel:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def add(self, tag):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO tag (name, color, id_user) VALUES (?, ?, ?);
        """, (tag.name, tag.color, tag.user.id))
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

    def get_by_name(self, name, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE name = ? AND id_user = ?;
        """, (name, user_id))
        
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def change_name(self, id, new_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE tag SET name = ? WHERE id = ?;
        """, (new_name, id))
        conn.commit()
        conn.close()
        return True
    
    def delete_by_name(self, name, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM tag WHERE name = ? AND id_user = ?;
        """, (name, user_id))
        conn.commit()
        conn.close()
        return True

    #-------------------------Color-------------------------------

    def get_by_color(self, color, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE color = ? AND id_user = ?;
        """, (color, user_id))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def change_color(self, id, new_color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE tag SET color = ? WHERE id = ?;
        """, (new_color, id))
        conn.commit()
        conn.close()
        return True

    def delete_by_color(self, color, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM tag WHERE color = ? AND id_user = ?;
        """, (color, user_id))
        conn.commit()
        conn.close()
        return True

    #-------------------------id_user-------------------------------

    def get_by_user(self, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM tag WHERE id_user = ?;
        """, (id_user,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def delete_by_user(self, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM tag WHERE id_user = ?;
        """, (id_user,))
        conn.commit()
        conn.close()
        return True


def convert_to_dict(rows):
    result = []
    for row in rows:
        result.append({
            'id': row[0],
            'name': row[1],
            'color': row[2],
            'id_user': row[3]
        })
    return result