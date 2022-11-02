import sqlite3

class UserTaskModel:
    def __init__(self):
        self.db_name = "src/Database/database.db"

    def add(self, user_task):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO user_task (id, user_id, task_id,role) VALUES (?,?, ?, ?);
        """, (user_task.id,user_task.user_id, user_task.task_id, user_task.role))
        conn.commit()
        conn.close()
        return True

    def get_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user_task;
        """)
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def delete_all(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user_task;
        """)
        conn.commit()
        conn.close()
        return True

    #-------------------------Id-------------------------------

    def get_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user_task WHERE id = ?;
        """, (id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def get_id_by_user_id(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id FROM user_task WHERE user_id = ?;
        """, (user_id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def get_id_by_task_id(self, task_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id FROM user_task WHERE task_id = ?;
        """, (task_id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def delete_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user_task WHERE id = ?;
        """, (id,))
        conn.commit()
        conn.close()
        return True

    #-------------------------User_id-------------------------------

    def get_by_user_id(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user_task WHERE user_id = ?;
        """, (user_id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def get_user_id_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT user_id FROM user_task WHERE id = ?;
        """, (id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def get_user_id_by_task_id(self, task_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT user_id FROM user_task WHERE task_id = ?;
        """, (task_id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def delete_by_user_id(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user_task WHERE user_id = ?;
        """, (user_id,))
        conn.commit()
        conn.close()
        return True

    #-------------------------Task_id-------------------------------

    def get_by_task_id(self, task_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user_task WHERE task_id = ?;
        """, (task_id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def get_task_id_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT task_id FROM user_task WHERE id = ?;
        """, (id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def get_task_id_by_user_id(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT task_id FROM user_task WHERE user_id = ?;
        """, (user_id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def delete_by_task_id(self, task_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user_task WHERE task_id = ?;
        """, (task_id,))
        conn.commit()
        conn.close()
        return True

    #-------------------------Role-------------------------------

    def get_by_role(self, role):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user_task WHERE role = ?;
        """, (role,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def get_role_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT role FROM user_task WHERE id = ?;
        """, (id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def get_role_by_user_id(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT role FROM user_task WHERE user_id = ?;
        """, (user_id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def get_role_by_task_id(self, task_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT role FROM user_task WHERE task_id = ?;
        """, (task_id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def delete_by_role(self, role):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user_task WHERE role = ?;
        """, (role,))
        conn.commit()
        conn.close()
        return True

def convert_to_dict(rows):
    dic = []
    for row in rows:
        dic.append({
            "id": row[0],
            "user_id": row[1],
            "task_id": row[2],
            "role": row[3]
        })
    return dic