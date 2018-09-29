import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("maxwell","mkimutai@123")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"maxwell")
        self.assertEqual(self.new_user.password,"mkimutai@123")

    def test_register_user(self):
        '''
        test_register_user test case to test if the user object is added to the user list
        '''
        self.new_user.register_user()  # saving the new username
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()
