from user import User


class Users:
    def __init__(self):
        self.users = []

    def user_in(self, tg_id: int) -> bool:
        for user in self.users:
            if user.id == tg_id:
                return True

        return False

    def add_user(self, user: User):
        self.users.append(user)

    def get(self, tg_id: int):
        for user in self.users:
            if user.id == tg_id:
                return User

        return None

    def update(self, user_to_update):
        for user in self.users:
            if user.id == user_to_update.id:
                self.users.remove(user)

        self.add_user(user_to_update)
