import sqlite3

class TaskModel:
    def __init__(self, db_name):
        self.db_name = db_name

    def add(self, task):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO task (name, description, state, date, priority, color, id_tag, id_user) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, (task.name, task.description, task.state, task.date, task.priority, task.color, task.tag.id, task.user.id))
        conn.commit()
        conn.close()
        return True

    #-------------------------Id---------------------------------

    def get_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE id = ?;
        """, (id,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def delete_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM task WHERE id = ?;
        """, (id,))
        conn.commit()
        conn.close()
        return True

    #-------------------------Name-------------------------------

    def get_by_name(self, name, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE name = ? AND id_user = ?;
        """, (name, id_user))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def change_name(self, name, new_name, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE task SET name = ? WHERE name = ? AND id_user = ?;
        """, (new_name, name, id_user))
        conn.commit()
        conn.close()
        return True

    def delete_by_name(self, name, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM task WHERE name = ? AND id_user = ?;
        """, (name, id_user))
        conn.commit()
        conn.close()
        return True

    #-------------------------Description------------------------

    def change_description(self, id, new_description):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE task SET description = ? WHERE id = ?;
        """, (new_description, id))
        conn.commit()
        conn.close()
        return True

    #-------------------------State-------------------------------

    def get_by_state(self, state, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE state = ? AND id_user = ?;
        """, (state, id_user))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def change_state(self, id, new_state):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE task SET state = ? WHERE id = ?;
        """, (new_state, id))
        conn.commit()
        conn.close()
        return True

    def delete_by_state(self, state, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM task WHERE state = ? AND id_user = ?;
        """, (state, id_user))
        conn.commit()
        conn.close()
        return True

    #-------------------------Date-------------------------------

    def get_by_date(self, date, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE date = ? AND id_user = ?;
        """, (date, id_user))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def change_date(self, id, new_date):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE task SET date = ? WHERE id = ?;
        """, (new_date, id))
        conn.commit()
        conn.close()
        return True

    def delete_by_date(self, date, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM task WHERE date = ? AND id_user = ?;
        """, (date, id_user))
        conn.commit()
        conn.close()
        return True

    #-------------------------Priority-------------------------------
    
    def get_by_priority(self, priority, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE priority = ? AND id_user = ?;
        """, (priority, id_user))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def change_priority(self, id, new_priority):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE task SET priority = ? WHERE id = ?;
        """, (new_priority, id))
        conn.commit()
        conn.close()
        return True

    def delete_by_priority(self, priority, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM task WHERE priority = ? AND id_user = ?;
        """, (priority, id_user))
        conn.commit()
        conn.close()
        return True

    #-------------------------Color-------------------------------

    def get_by_color(self, color, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE color = ? AND id_user = ?;
        """, (color, id_user))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def change_color(self, id, new_color):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE task SET color = ? WHERE id = ?;
        """, (new_color, id))
        conn.commit()
        conn.close()
        return True

    def delete_by_color(self, color, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM task WHERE color = ? AND id_user = ?;
        """, (color, id_user))
        conn.commit()
        conn.close()
        return True

    #-------------------------Tag-------------------------------
    
    def get_by_tag(self, tag, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE id_tag = ? AND id_user = ?;
        """, (tag, id_user))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def change_tag(self, id, new_tag):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE task SET id_tag = ? WHERE id = ?;
        """, (new_tag, id))
        conn.commit()
        conn.close()
        return True

    def delete_by_tag(self, tag, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM task WHERE id_tag = ? AND id_user = ?;
        """, (tag, id_user))
        conn.commit()
        conn.close()
        return True

    #-------------------------User-------------------------------

    def get_by_user(self, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM task WHERE id_user = ?;
        """, (id_user,))

        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        
        return dic

    def delete_by_user(self, id_user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM task WHERE id_user = ?;
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
            'description': row[2],
            'state': row[3],
            'date': row[4],
            'priority': row[5],
            'color': row[6],
            'id_tag': row[7],
            'id_user': row[8]
        })
    return result
    