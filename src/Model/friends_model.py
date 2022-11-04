import sqlite3

class FriendsModel:
    def __init__(self, db_name):
        self.db_name = db_name

    def add(self, friend):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO friends (id,id_user_1, id_user_2, state) VALUES (?,?, ?, ?);
        """, (friend.id,friend.id_user_1, friend.id_user_2, friend.state))
        conn.commit()
        conn.close()
        return True

    #-------------------------Id-------------------------------

    def get_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM friends WHERE id = ?;
        """, (id,))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def delete_by_id(self, id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM friends WHERE id = ?;
        """, (id,))
        conn.commit()
        conn.close()
        return True

    def get_id(self, user_id_1, user_id_2):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id FROM friends WHERE id_user_1 = ? AND id_user_2 = ?;
        """, (user_id_1, user_id_2))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    #-------------------------Id_user_1-------------------------------

    def get_by_user(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM friends WHERE id_user_1 = ? ;
        """, (user_id))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic

    def delete_by_user(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM friends WHERE id_user_1 = ?;
        """, (user_id,))
        conn.commit()
        conn.close()
        return True


    #-------------------------State-------------------------------

    def get_by_state(self, user_id,state):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM friends WHERE id_user_1 = ? AND state = ?;
        """, (user_id,state))
        dic = convert_to_dict(cursor.fetchall())
        conn.close()
        return dic
       
    def change_state(self, id, state):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE friends SET state = ? WHERE id = ?;
        """, (state, id))
        conn.commit()
        conn.close()
        return True

    def delete_by_state(self,user_id,state):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM friends WHERE id_user_1 = ? AND state = ?;
        """, (user_id,state))
        conn.commit()
        conn.close()
        return True


def convert_to_dict(rows):
    result = []
    for row in rows:
        d = {
            'id': row[0],
            'id_user_1': row[1],
            'id_user_2': row[2],
            'state': row[3]
            
        }
        result.append(d)
    return result
    