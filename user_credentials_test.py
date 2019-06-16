import unittest
from user_credentials import User
class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Js', "123abc")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
    def test__init__(self):
        '''
        test__init__ test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Js")
        self.assertEqual(self.new_user.password,"123abc")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User('Test', 'User123')
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


if __name__ == "__main__":
        
    unittest.main()