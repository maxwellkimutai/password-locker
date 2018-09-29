class User:
    '''
    Class that generates new instances of a user
    '''

    user_list = []

    def __init__(self,username,password):
        '''
        __init__ method that helps us define properties for our object


        Args:
            username: New user username
            password: New user password
        '''

        self.username = username
        self.password = password

    
