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

    def save_credential(self):
        '''
        save_contact method saves credential objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    @classmethod
    def generate_password(cls):
        '''
        generate_password method generates a password for the new account
        '''
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

        password = ''.join(random.choice(chars) for _ in range(10))

        return password

    @classmethod
    def display_credentials(cls):
        '''
        display_credentials method returns the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def find_by_account(cls,account):
        '''
        find_by_account method takes in an account name and returns all the accounts with that name

        Args:
            account: name of the account to search for

        Returns:
            Details of accounts with the account name
        '''

        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
