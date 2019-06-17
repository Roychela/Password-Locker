import random
import string
import pyperclip 
class User:
    """
    Class that generates new instances of users.
    """
    user_list = []
    def __init__(self, username, password):
        """
        Init method that gives the blueprint of the objects to be instantiated
        """
        self.username = username
        self.password = password
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
class Credentials:
    '''
    Class that defines the credentials class behaviours.
    '''
    credentials_list = []
    user_credentials_list = []
    @classmethod
    def confirm_login(cls, username, password):
        '''
        Method for login functionality.
        '''
        current_user = '' 
        for user in User.user_list:
            if user.username == username and user.password == password:
                current_user = user.username
        return current_user
        
    def __init__(self,user_name,site_name,account_name,password):
        '''
        Method to define the properties for each user object will hold.
        '''
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password
    def save_credentials(self):
        '''
        Function to save a user credentials instance
        '''
        Credentials.credentials_list.append(self)
    @classmethod
    def display_credentials(cls,user_name):
        '''
        Function to display saved credentials
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    def generate_password(size=8, char=string.ascii_lowercase+string.ascii_uppercase+string.digits):
        '''
        Function to generate random password
        '''
        passwrd_generated=''.join(random.choice(char) for _ in range(size))
        return passwrd_generated
    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        Function that finds a credential based on the site_name
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential
                
    @classmethod
    def copy_credential(cls,site_name):
        '''
        Function that copies a credential
        '''
        find_credential = Credentials.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)
