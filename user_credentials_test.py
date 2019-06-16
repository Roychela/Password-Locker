import unittest
from user_credentials import User
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Js', "123abc")
    def tearDown(self):
        User.user_list = []
    def test__init__(self):
        self.assertEqual(self.new_user.username,"Js")
        self.assertEqual(self.new_user.password,"123abc")
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User('Test', 'User123')
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


if __name__ == "__main__":
        
    unittest.main()