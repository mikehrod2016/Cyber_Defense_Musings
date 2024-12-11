'''This program by the admirable Michael Rodriguez, creates webpages using Python Flasks'''

import string
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import flash

APP = Flask(__name__)
APP.secret_key = "♩a whole new key♩"
CURRENT_TIME = datetime.now().strftime("%d%b%Y  %X")
LOWER_CASE_LETTERS = string.ascii_lowercase
UPPER_CASE_LETTERS = string.ascii_uppercase
NUMBERS = string.digits
SPECIAL_CHARACTERS = string.punctuation

class LoginCookieMaker:
    '''Creates a login cookie in relation to the current user.'''
    username = ''
    def __init__(self, loginStatus=False):
        '''Initializes login status'''
        self.loginStatus = loginStatus
    def getLoginStatus(self):
        '''Retrieves current login status'''
        return self.loginStatus
    def setLoginStatus(self, currentStatus):
        '''Sets a new login status'''
        self.loginStatus = currentStatus
    @classmethod
    def getUsername(cls):
        '''Returns username'''
        return cls.username
    @classmethod
    def setUsername(cls, newUsername):
        '''Sets a new username'''
        cls.username = newUsername

loginCookie = LoginCookieMaker()

@APP.route("/", methods=['GET', 'POST'])
def loginPage():
    '''Renders the login page'''

    #Checks credentials
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        userAccount = username + ":" + password

        accountsFile = open('accountsFile.txt', "r")
        accounts = accountsFile.read()
        accountsFile.close()

        #Updates login cookie if correct credentials
        if userAccount in accounts and password not in ['', None] and username not in ['', None]:
            loginCookie.setLoginStatus(True)
            loginCookie.setUsername(username)
            return redirect('/home')
        flash('Invalid Credentials')
        #Log failed login attempt
        logFile = open('logFile.txt', 'a')
        logTime = datetime.now().strftime("[%d%b%Y] %X ")
        logEntry = logTime + request.remote_addr + '\n'
        logFile.write(logEntry)
        logFile.close()

    return render_template('login.html', currentDate=CURRENT_TIME)

@APP.route("/home")
def homePage():
    '''Renders the kittens vs ninja stars home page'''
    if not loginCookie.getLoginStatus():
        return redirect('/')
    return render_template('home.html', currentDate=CURRENT_TIME)

@APP.route('/kittens')
def kittensPage():
    '''Renders the kittens page'''
    if not loginCookie.getLoginStatus():
        return redirect('/')
    return render_template('kittens.html', currentDate=CURRENT_TIME)

@APP.route('/ninjaStars')
def ninjaStarspage():
    '''Renders the Ninja Stars page'''
    if not loginCookie.getLoginStatus():
        return redirect('/')
    return render_template('ninjaStars.html', currentDate=CURRENT_TIME)

@APP.route('/registration', methods=['GET', 'POST'])
def register():
    '''Renders the registration page'''


    #Litany of password checks
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmedPassword = request.form["confirmedPassword"]
        error = None

        commonPasswordsFile = open('CommonPassword.txt', 'r')
        commonPasswords = commonPasswordsFile.read()

        accountsFile = open('accountsFile.txt', "r")
        accounts = accountsFile.read()

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif password != confirmedPassword:
            error = "Your passwords do not match."
        elif password in commonPasswords:
            error = 'You must not use a common password.'
        elif len(password) < 12:
            error = 'Your password must be at least 12 characters.'
        elif characterCheck(password, LOWER_CASE_LETTERS):
            error = "You must have a lower case letter."
        elif characterCheck(password, UPPER_CASE_LETTERS):
            error = "You must have an upper case letter."
        elif characterCheck(password, NUMBERS):
            error = "You must have a number."
        elif characterCheck(password, SPECIAL_CHARACTERS):
            error = "You must have a special character."
        elif username in accounts:
            error = 'Account already exists.'
        flash(error)

        #Store valid credentials
        if error is None:
            commonPasswordsFile.close()
            accountsFile.close()

            accountsFile = open('accountsFile.txt', 'a')
            accountsFile.write(username + ":" + password + "\n")
            accountsFile.close()

            loginCookie.setLoginStatus(True)
            loginCookie.setUsername(username)
            return redirect('/home')
    return render_template('registration.html', currentDate=CURRENT_TIME)

@APP.route('/updatePassword', methods=['GET', 'POST'])
def updatePassword():
    '''Renders the update password page'''
    if not loginCookie.getLoginStatus():
        return redirect('/home')

    commonPasswordsFile = open('CommonPassword.txt', 'r')
    commonPasswords = commonPasswordsFile.read()

    #Litany of password checks
    if request.method == "POST":
        passwordToChange = request.form["passwordToChange"]
        newPassword = request.form["newPassword"]
        confirmedPassword = request.form["confirmedPassword"]
        error = None

        oldAccount = loginCookie.getUsername() + ":" + passwordToChange + "\n"
        accountsFile = open('accountsFile.txt', "r")
        accounts = accountsFile.read()

        if not passwordToChange:
            error = "You must enter your current password."
        elif oldAccount not in accounts:
            error = 'Invalid current password.'
        elif newPassword != confirmedPassword:
            error = "Your passwords do not match."
        elif not newPassword or not confirmedPassword:
            error = 'You must enter a new password and confirm it.'
        elif newPassword+'\n' in commonPasswords:
            error = 'You must not use a common password.'
        elif len(newPassword) < 12:
            error = 'Your password must be at least 12 characters.'
        elif characterCheck(newPassword, LOWER_CASE_LETTERS):
            error = "You must have a lower case letter."
        elif characterCheck(newPassword, UPPER_CASE_LETTERS):
            error = "You must have an upper case letter."
        elif characterCheck(newPassword, NUMBERS):
            error = "You must have a number."
        elif characterCheck(newPassword, SPECIAL_CHARACTERS):
            error = "You must have a special character."
        flash(error)

        #Store valid credentials
        if error is None:
            newAccount = loginCookie.getUsername() + ":" + newPassword + "\n"

            accountsFile = open('accountsFile.txt', "w")
            accounts = accounts.replace(oldAccount, newAccount)
            accountsFile.write(accounts)
            accountsFile.close()
            return redirect('/home')
    return render_template('updatePassword.html', currentDate=CURRENT_TIME)

def characterCheck(password, characterSet):
    '''Checks the occurrences of a specific type of character'''
    totalCases = 0

    for character in characterSet:
        totalCases += password.count(character)
    missingCheck = totalCases == 0

    return missingCheck

if __name__ == '__main__':
    APP.debug = True
    APP.run()
