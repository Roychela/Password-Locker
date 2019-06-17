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
def create_credential(user_name,site_name,account_name,password):
    '''
    Function to create a new credential object
    '''
    new_credential = Credentials(user_name,site_name,account_name,password)
    return new_credential
def save_credential(credential):
    '''
    Function to save a created credential
    '''
    Credentials.save_credentials(credential)
def generate_password():
    '''
    Function to randomly generate password
    '''
    passwrd_generated = Credentials.generate_password()
    return passwrd_generated
def display_credentials(user_name):
    '''
    Function to display credentials
    '''
    return Credentials.display_credentials(user_name)
def copy_credential(site_name):
    '''
    Function to copy a credential to the clipboard
    '''
    return Credentials.copy_credential(site_name)


def main():
    print(' ')
    print('Hello! Welcome to Password Locker.')
    while True:
        print(' ')
        print("-"*40)
        print('Use these short codes: ca-Create Password-Locker account,  log-Login, ex-Exit')
        short_code = input('Enter short code here: ').lower().strip()
        if short_code == 'ex':
            break
        elif short_code == 'ca':
            print("-"*40)
            print(' ')
            print('To create a new account:')
            username = input('Choose a username - ').strip()
            password = input('Choose a password - ').strip()
            save_user(create_user(username,password))
            print(" ")
            print(f'Your Password-Locker account username is : {username}  and password is: {(password)}')
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
                    elif short_code == 'ccd':
                        print(' ')
                        print('Enter your credential account information:')
                        site_name = input('Enter the site name- ').strip()
                        account_name = input('Enter your account name - ').strip()
                        while True:
                            print(' ')
                            print("-"*40)
                            print('Select option for entering a password:  ep-Enter your own password, gp-Generate a password ,ex-Exit')
                            passwrd_select = input('Enter an option: ').lower().strip()
                            print("-"*40)
                            if passwrd_select == 'ep':
                                print(" ")
                                password = input('Enter your password: ').strip()
                                break
                            elif passwrd_select == 'gp':
                                password = generate_password()
                                break
                            elif passwrd_select == 'ex':
                                break
                            else:
                                print('Incorrect entry. Try again.')
                        save_credential(create_credential(user_name,site_name,account_name,password))
                        print(' ')
                        print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
                        print(' ')
                    elif short_code == 'dc':
                        print(' ')
                        if display_credentials(user_name):
                            print('Your credentials account list:')
                            print(' ')
                            for credential in display_credentials(user_name):
                                print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                            print(' ')
                        else:
                            print(' ')
                            print("No credentials saved")
                            print(' ')
                    elif short_code == 'cp':
                        print(' ')
                        chosen_site = input('Enter the site name for the credential password to copy: ')
                        copy_credential(chosen_site)
                        print('')
                        print('Paste copied site_name password here:')
                        copy = input()
                    else:
                        print('Incorrect entry.Try again.')
            else: 
                print(' ')
                print('Incorrect entry. Try again or Create an Account.')		
        else:
            print("-"*40)
            print(' ')
            print('Incorrect entry. Try again.')
				
if __name__ == "__main__":
    main()