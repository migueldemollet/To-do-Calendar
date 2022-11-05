import sqlite3

class UserTaskModel:
    def __init__(self, db_name):
        self.db_name = db_name

    def add(self, user, task, role):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO user_task (user_id, task_id, role) VALUES (?, ?, ?);
        """, (user.id, task.id, role))
        conn.commit()
        conn.close()
        return True
    
    def check_user_task(self, user_id, task_id, role):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user_task WHERE user_id = ? AND task_id = ? AND role = ?;
        """, (user_id, task_id, role))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic
    
    def delete_by_user_task_role(self, user_id, task_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user_task WHERE user_id = ? AND task_id = ? AND role = 1;
        """, (user_id, task_id))
        conn.commit()
        conn.close()
        return True

    #-------------------------User_id-------------------------------

    def get_by_user(self, user_id, role):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user_task WHERE user_id = ? AND role = ?;
        """, (user_id, role))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def delete_by_user(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user_task WHERE user_id = ?;
        """, (user_id,))
        conn.commit()
        conn.close()
        return True

    #-------------------------Task_id-------------------------------

    def get_by_task(self, task_id, role):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user_task WHERE task_id = ? AND role = ?;
        """, (task_id, role))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def delete_by_task(self, task_id):
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