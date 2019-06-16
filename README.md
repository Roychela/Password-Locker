# Password-Locker

##By Roy Chela

## Description
Password Locker is an application that will help users manage their passwords and even generate new passwords.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for sign up and log in | **In terminal: $./run.py** |Use these short codes: ca-Create Password-locker Account, log-login, ex-Exit |
| Display input prompt for creating an account |Type in ca short code and choose a username and password|Your username is x and password is y |
| Display input prompt for login|Type in log short code and enter the username and password earlier created| You have successfully logged in. Choose short code to continue |
| Display codes for credentials| Successfully logged in| Select short code: ccd - create credential, dc - display Credentials, dl - delete credential, cp - copy credential, ex - exit |
| Display input prompt for creating a credential |Type in ccd short code and enter the site name, site-account  username and password | Displays the site name, site-account-username and password |
| Display a list of credentials |Type in dc short code | Displays a list of saved account credentials |
| Display input prompt for which credential account to delete |Type in dl short code | Deletes the selected credential account|
| Display input prompt for which credential to copy |Type in cp short code | Copies the credential|
| Exit application |Type in ex short code| Exits current location |

## SetUp Requirements
### Prerequisites
* pyperclip
* xclip

### Cloning
* In your terminal:

        $ git clone https://github.com/roychela/Password-Locker/
        $ cd Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x run.py
        $ ./run.py

## Testing the Application
* To run the tests for the classes

        $ python3.6 user_credentials_test.py

## Technologies Used
* Python3.6

## Support and contact details

If you run into any issues or have questions, ideas or concerns contact roychela@gmail.com

## License
MIT Copyright (c) 2019 Roy Chela
