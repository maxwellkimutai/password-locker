#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def register(uname,pword):
    '''
    Function to create a new user
    '''
    new_user = User(uname,pword)
    new_user.register_user()

def create_account(account,login,password,user):
    '''
    Function to add an existing account
    '''
    new_credential = Credentials(account,login,password,user)
    return new_credential

def save_account(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credential()

def generate_a_password():
    '''
    Function to generate a password for the user account
    '''
    return Credentials.generate_password()

def display_credential():
    '''
    Function to return all the saved credentials
    '''
    return Credentials.display_credentials()

def find_account(account):
    '''
    Function to find an account
    '''
    return Credentials.find_by_account(account)
