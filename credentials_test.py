import unittest # Importing the unittest module
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Credentials("Facebook","kace","12345","maxwell")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account,"Facebook")
        self.assertEqual(self.new_account.login,"kace")
        self.assertEqual(self.new_account.password,"12345")
        self.assertEqual(self.new_account.user,"maxwell")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credentials list
        '''
        self.new_account.save_credential() # saving the new credential
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple contact
        objects to our credentials_list
        '''
        self.new_account.save_credential()
        test_account = Credentials("Test","user","55555","maxwell") # new contact
        test_account.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_generate_password_not_empty(self):
        '''
        test_generate_password_not_empty to check if the password is generated
        '''
        self.assertEqual(len(Credentials.generate_password()),10)

    
