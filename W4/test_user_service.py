import unittest
from datetime import datetime
from user import User
from user_service import UserService


class TestUserService(unittest.TestCase):

    def test_add_and_find_user(self):
        user = User(100, "Jane", "Smith", datetime(1999, 5, 5))
        UserService.add_user(user)
        found = UserService.find_user(100)
        self.assertEqual(found.name, "Jane")

    def test_delete_user(self):
        user = User(200, "Mark", "Lee", datetime(1995, 3, 3))
        UserService.add_user(user)
        self.assertTrue(UserService.delete_user(200))


if __name__ == "__main__":
    unittest.main()