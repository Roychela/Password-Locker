global user_list
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
    def confirm_login(self):

        '''
        Method for login functionality.
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
        

