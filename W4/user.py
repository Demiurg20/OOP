from datetime import datetime, date


class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = None
        self.password = None

    def get_details(self):
        return (f"ID: {self.user_id}\n"
                f"Name: {self.name} {self.surname}\n"
                f"Email: {self.email}\n"
                f"Age: {self.get_age()}")

    def get_age(self):
        today = date.today()
        return today.year - self.birthday.year - (
            (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )