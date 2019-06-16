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
        User.user_list.append(self)