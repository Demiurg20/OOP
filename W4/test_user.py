import unittest
from datetime import datetime
from user import User


class TestUser(unittest.TestCase):

    def test_age(self):
        user = User(1, "John", "Doe", datetime(2000, 1, 1))
        self.assertTrue(user.get_age() >= 20)

    def test_details(self):
        user = User(1, "John", "Doe", datetime(2000, 1, 1))
        self.assertIn("John Doe", user.get_details())


if __name__ == "__main__":
    unittest.main()