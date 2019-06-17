
#global user_list
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
    credentials_list =[]
    user_credentials_list = []
    @classmethod
    def confirm_login(cls, username, password):

        '''
        Method for login functionality.
        '''
        current_user = '' 
        for user in cls.user_list:
          
            if user.username == username and user.password == password:
                current_user == user.username
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