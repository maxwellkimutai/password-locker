import random
class Credentials:
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    credentials_list = []

    def __init__(self,account,login,password,user):
        '''
        __init__ method that helps us define properties for our object


        Args:
            account: New user account for login and password
            login: New account login
            password: New account password
        '''
        self.account = account
        self.login = login
        self.password = password
        self.user = user

    
