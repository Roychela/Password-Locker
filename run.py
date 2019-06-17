#!/usr/bin/env python3.6
from user_credentials import User
from user_credentials import Credentials 
def create_user(uname,password):
    '''
    Function to create a new user
    '''
    new_user = User(uname, password)
    return new_user
def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def authenticate_user(username, password):
    '''
    Function to authenticate a user
    '''
    authenticated_user = Credentials.confirm_login(username, password)
    return authenticated_user


def main():
    print(' ')
    print('Hello! Welcome to Password Locker.')
    while True:
        print(' ')
        print("-"*40)
        print('Use these short codes: ca-Create Password-Locker account,  log-Login, ex-Exit')
        short_code = input('Enter short code here: ').lower().strip()
        if short_code == 'ca':
            print("-"*40)
            print(' ')
            print('To create a new account:')
            username = input('Choose a username - ').strip()
            password = input('Choose a password - ').strip()
            save_user(create_user(username,password))
            print(" ")
            print(f'Your Password-Locker account username is : {username}  and password is: {password}')
        elif short_code == 'ex':
            break
        elif short_code == 'log':
            print("-"*40)
            print(' ')
            print('To login:')
            user_name = input('Enter your Password-Locker username - ').strip()
            password = str(input('Enter your password - '))
            user_authenticated = authenticate_user(user_name,password)
            if user_authenticated == user_name:
                print(" ")
                print(f'Welcome {user_name}. You have successfully logged in. Choose short code to continue')
                print(' ')
                while True:
                    print("-"*40)
                    print('Your credentials short codes: ccd-Create credential, dc-Display Credentials, dl-delete credentials account, cp-Copy Password, ex-Exit')
                    short_code = input('Enter short code: ').lower().strip()
                    print("-"*40)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Goodbye {user_name}')
                        break
if __name__ == "__main__":
    main()