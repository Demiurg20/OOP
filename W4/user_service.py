class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]
            return True
        return False

    @classmethod
    def update_user(cls, user_id, user_update):
        user = cls.users.get(user_id)
        if user:
            user.name = user_update.name
            user.surname = user_update.surname
            user.birthday = user_update.birthday
            return True
        return False

    @classmethod
    def get_number(cls):
        return len(cls.users)