from user import User


class Users:
    def __init__(self):
        self.users = []

    def user_in(self, tg_id: int) -> bool:
        """возвращает признак того, что пользователь пользовался ботом"""
        for user in self.users:
            if user.id == tg_id:
                return True

        return False

    def add_user(self, user: User):
        """добавляет пользователя в список"""
        self.users.append(user)

    def get(self, tg_id: int):
        """возвращает объект типа User по telegram_id"""
        for user in self.users:
            if user.id == tg_id:
                return User

        return None

    def update(self, user_to_update):
        """обновляет информацию о пользователе"""
        for user in self.users:
            if user.id == user_to_update.id:
                self.users.remove(user)

        self.add_user(user_to_update)
