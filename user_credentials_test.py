import unittest
from user_credentials import User
from user_credentials import Credentials
class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Js', "123abc")
    def tearDown(self):
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
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def test_confirm_login(self):

        '''
        Method to test login functionality.
        '''
        self.new_user = User('Js','123abc')
        self.new_user.save_user()
        test_user = User('Test', 'User123')
        test_user.save_user()
        for user in User.user_list:
            current_user = ''
            if user.username == test_user.username and user.password == test_user.password:
                current_user == user.username
        return current_user
        self.assertEqual(current_user, Credentials.confirm_login(test_user.username, test_user.password))

    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credentials('Js','Instagram','@jst','123abc')
    def test__init__(self):
        '''
        test__init__ test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,'Js')
        self.assertEqual(self.new_credential.site_name,'Instagram')
        self.assertEqual(self.new_credential.account_name,'@jst')
        self.assertEqual(self.new_credential.password,'123abc')
    def test_save_credentials(self):
        '''
        Test to confirm if the new credential is saved to the credentials list
        '''
        self.new_credential.save_credentials()
        instagram = Credentials('Mike','Instagram','mikay','123abc')
        instagram.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2) 
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
        User.user_list = []
        
    def test_display_credentials(self):
        '''
        Test to check if credentials display method displays
        '''
        self.new_credential.save_credentials()
        instagram = Credentials('Mike','Instagram','mikay','abc')
        instagram.save_credentials()
        facebook = Credentials('Mg','Facebook','mikay','123efg')
        facebook.save_credentials()
        self.assertEqual(len(Credentials.display_credentials(instagram.user_name)), 1)
	 
    def test_find_by_site_name(self):
        '''
        Test method for finding a credential site_name
        '''
        self.new_credential.save_credentials()
        instagram = Credentials('Mike','Instagram','mikay','abc')
        instagram.save_credentials()
        credential_exists = Credentials.find_by_site_name('Instagram')
        self.assertEqual(credential_exists, Credentials.find_by_site_name('Instagram') )




if __name__ == "__main__":
        
    unittest.main()