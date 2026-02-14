import unittest
from user_util import UserUtil


class TestUserUtil(unittest.TestCase):

    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertEqual(len(str(user_id)), 9)

    def test_password_strength(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password))

    def test_email_validation(self):
        self.assertTrue(UserUtil.validate_email("john.doe@test.com"))
        self.assertFalse(UserUtil.validate_email("wrong_email"))


if __name__ == "__main__":
    unittest.main()