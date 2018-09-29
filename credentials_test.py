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

    
