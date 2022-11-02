import sqlite3

class UserModel:
    def __init__(self, db_name):
        self.db_name = db_name

    def add(self, user):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO user (id, name, email, password ) VALUES (?,?, ?, ?);
        """, (user.id,user.name, user.email, user.password))
        conn.commit()
        conn.close()
        return True

    #-------------------------Id-------------------------------

    def get_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user WHERE id = ?;
        """, (id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def delete_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user WHERE id = ?;
        """, (id,))
        conn.commit()
        conn.close()
        return True

    #-------------------------Username-------------------------------

    def get_by_username(self, username):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user WHERE username = ?;
        """, (username,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def change_username(self, id, new_username):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE user SET username = ? WHERE id = ?;
        """, (new_username, id))
        conn.commit()
        conn.close()
        return True

    def delete_by_username(self, username):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user WHERE username = ?;
        """, (username,))
        conn.commit()
        conn.close()
        return True

    #-------------------------Email-------------------------------

    def get_by_email(self, email):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM user WHERE email = ?;
        """, (email,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def change_email(self, id, new_email):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE user SET email = ? WHERE id = ?;
        """, (new_email, id))
        conn.commit()
        conn.close()
        return True

    def delete_by_email(self, email):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user WHERE email = ?;
        """, (email,))
        conn.commit()
        conn.close()
        return True

    #-------------------------Password-------------------------------

    def change_password(self, id, new_password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE user SET password = ? WHERE id = ?;
        """, (new_password, id))
        conn.commit()
        conn.close()
        return True


def convert_to_dict(rows):
    result = []
    for row in rows:
        d = {
            'id': row[0],
            'username': row[1],
            'email': row[2],
            'password': row[3]
        }
        result.append(d)
    return result