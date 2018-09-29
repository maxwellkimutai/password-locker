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
def main():
    print("Hello, welcome to password locker. Please register an account.")
    print("Enter your username:")
    pl_user_name = input()

    print("Enter your password:")
    password = input()
    print("\n")

    register(pl_user_name,password)

    while True:
        print("\n")
        print("Use the words : add - add a new account, display - display all accounts, find - find an account, exit - exit the program")

        selected_word = input().lower()

        if selected_word == 'add':
            print("Add Account")
            print("-"*10)

            print("Enter the account/application name: ")
            account = input()

            print("Enter the login/username")
            login = input()

            while True:
                print("Would you like us to generate a password for you?(y/n)")
                response = input().lower()

                if response == "y":
                    password = generate_a_password()

                    print(f"Your password is {password}")
                    break
                elif response == "n":
                    print("\n")
                    print("Enter a password: ")
                    password = input()
                    break
                else:
                    print("\n")
                    print("Invalid input. Please try again.")

            save_account(create_account(account,login,password,pl_user_name))

        elif selected_word == 'display':
            print("Please enter your username")
            u_name = input()
            print("Please enter your password")
            p_word = input()

            for user in User.user_list:
                if user.username == u_name:
                    if user.password == p_word:
                        if display_credential():
                            print("The following is a list of all your accounts")
                            print("\n")

                            for account in display_credential():
                                print("-"*10)
                                print(f"Account: {account.account}")
                                print(f"Login: {account.login}")
                                print(f"Password: {account.password}")

                        else:
                            print('\n')
                            print("You dont seem to have any contacts saved yet")
                            print('\n')

        elif selected_word == 'find':
            print("\n")
            print("Enter the account name")
            acc_name = input()

            if find_account(acc_name):
                found_account = find_account(acc_name)
                print("-"*10)
                print(f"Account: {found_account.account}")
                print(f"Login: {found_account.login}")
                print(f"Password: {found_account.password}")

        elif selected_word == 'exit':
            print("\n")
            print("Thank you for using password generator")
            break

        else:
            print("\n")
            print("Invalid input. Please try again")
            print("\n")

if __name__ == '__main__':
    main()
