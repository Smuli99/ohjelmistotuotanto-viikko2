from entities.user import User
import re


class UserRepository:
    def __init__(self):
        self._users = []

    def find_all(self):
        return self._users

    def find_by_username(self, username):
        users = self.find_all()

        users_with_username = filter(
            lambda user: user.username == username,
            users
        )

        users_with_username_list = list(users_with_username)

        return users_with_username_list[0] if len(users_with_username_list) > 0 else None

    def create(self, user):
        users = self.find_all()

        existing_user = self.find_by_username(user.username)
        
        if len(user.username) < 3:
            raise Exception(
                f"Username {user.username} must be at least 3 characters long"
            )

        if not re.match('^[a-z]{3,}$', user.username):
            raise Exception(
                f"Username {user.username} must only contain lowercase letters a to z"
            ) 

        existing_user = self.find_by_username(user.username)

        if existing_user:
            raise Exception(
                f"User with username {user.username} already exists"
            )

        if len(user.password) < 8:
            raise Exception(
                f"Password must be at least 8 characters long"
            )

        if not re.match('^(?=.*[0-9\W]).{8,}$', user.password):
            raise Exception(
                f"Password must contain number or special character"
            )

        users.append(user)

        self._users = users

        return user

    def delete(self, user_id):
        users = self.find_all()

        users_without_id = filter(lambda user: user.id != user_id, users)

        self._users = list(users_without_id)

    def delete_all(self):
        self._users = []
