import sys
sys.path.insert(1, 'Src/Model/')
from user_model import UserModel

class MochDb(UserModel):

    def get_by_username(self, username):
        if username == "test":
            return [{'id': 1, 'username': 'test', 'email': 'test@tdcalendar.com', 'password': '5e06b84ac4f276aa03afc04fd1e82856'}]
        else:
            return []

    