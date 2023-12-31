### Header ###
import re
import globalVars
import time
from database import *
from UI import *
from loginLanding import *

### Functions ###

def deleteUser():
  from landing import startupLanding
  
  username = input("\nEnter the username you want to delete: ")
  cursor.execute("SELECT username FROM users WHERE username=?", (username,))
  existing_user = cursor.fetchone()

  if existing_user:
    cursor.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()
    print(f"User {username} has been deleted.")
    startupLanding()
        
  else:
    print(f"User {username} not found in the database.")
    startupLanding()


def createUser():
    # Check if the maximum number of accounts has been reached
    cursor.execute("SELECT COUNT(*) FROM users")
    account_count = cursor.fetchone()[0]

    if account_count >= globalVars.maxActiveAccounts:
        print("All permitted accounts have been created. Please come back later.")
        choice = input("Do you want to delete an existing account? (yes/no): ")
        if choice.lower() == "yes":
            deleteUser()
        else:
            print("Please come back later.")
            userHome()
        return
        
    # This pattern ensures that our password will be: minimum of 8 characters, max of 12     
    # characters, 1 capital letter, 1 digit, 1 special character
    regexPattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$'
  
    username = input("\nPlease enter a username: ")
    cursor.execute("SELECT username FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()  # Check if the username already exists in the database
    if existing_user:
        print("Username already exists. Please choose a different username.")
        username = input("Please enter a username: ")
        
    counter1 = True
    while counter1: 
        password = input("Enter a password: ")
        #compares password input with regexPattern
        if re.match(regexPattern, password):
            storePassword = password
            break
        else:
            print("Invalid password type. Please enter a password that has a minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one special character")
          
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    major = input("Enter your major: ")
    uni= input("Enter your univeristy: ")
    
    # default user account settings to store into users entry on DB
    defaultEmail = True
    defaultSMS = True
    defaultAdTarget = True
    defaultLanguage = 0
    dateCreated = datetime.now()

    cursor.execute("INSERT INTO users (username, password, firstName, lastName, marketingEmail, marketingSMS, adsTargeted, language, userMajor , userUniversity, createDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (username, storePassword, firstName, lastName, defaultEmail, defaultSMS, defaultAdTarget, defaultLanguage, major, uni, dateCreated))
    conn.commit()  # Insert the new user into the 'users' table and commit the changes to the database
    print("Congratulations! Your account has been successfully registered.")

    
    #updating global user variables
    globalVars.isLoggedIn = True
    globalVars.username = username
    globalVars.userFirstName = firstName
    globalVars.userLastName = lastName
    globalVars.userMajor = major
    globalVars.userUniversity = uni
    #user tier functionality
    globalVars.userTier = userTierSelect()

    userHome()


def UserLogin():
    while True: 
        username = input("\nPlease enter your username: ")
        
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        # Retrieve user data from the database
        user_data = cursor.fetchone()  
        
        if not user_data:  # If the username is not found in the database
            print("The username you have entered does not exist. Please try again.")
            continue
        globalVars.currentUser = username

        # Get the correct password from the retrieved data
        correct_password = user_data[2]  
        counter = True
        while counter:
            password = input("Please enter your password: ")
            # Check if the entered password matches the correct password
            if password == correct_password:  
                print("You have successfully logged in.")
                counter = False
                
                #update the global user variables and settings
                globalVars.isLoggedIn = True
                globalVars.userID = user_data[0]
                globalVars.username = user_data[1]
                globalVars.userFirstName = user_data[3]
                globalVars.userLastName = user_data[4]
                globalVars.userSettingMarketingEmail = user_data[5]
                globalVars.userSettingMarketingSMS = user_data[6]
                globalVars.userSettingAdvertisementTargeted = user_data[7]
                globalVars.userSettingLanguage = user_data[8]
                globalVars.userMajor = user_data[11]
                globalVars.userTier = user_data[12]

                #update login dates
                LoginDatesUpdate()

                #move to logged in home menu
                userHome()
            else:
                print("Incorrect username/password. Please try again.")
                continue
        break

def userTierSelect():
    from billing import creditCardSetup
    from datetime import date
    selection = None
    print("Would you like to become an InCollege Plus Member?")
    print("For only $10 a month you get the following:")
    # Plus member benifit list
    print("*\tForge new connections with the ability to message")
    print(" \tany member without having to friend them.")

    while selection == None:
        userInput = input("Would you like to become a Plus Member? (y/n): ")
        subDate = date.today()
        if userInput.upper() == 'Y':
            creditCardSetup() #placeholder
            selection = 1
        elif userInput.upper() == 'N':
            selection = 0
            subDate = None
        else:
            print("Invalid Option. Try Again")
            time.sleep(1)

        # update user record for tier
        cursor.execute ("UPDATE users SET userTier = ?, subscriptionDate = ? WHERE username = ?",(selection, subDate, globalVars.username))
        conn.commit()

        return selection

def LoginDatesUpdate():
    import time
    
    #get the user's old "current" date
    cursor.execute("SELECT currentLoginDate FROM users WHERE userID = ?",(globalVars.userID,))
    result = cursor.fetchone()
    oldDate = result[0]
    
    #set the new current date
    newDate = datetime.now()

    #place old "current" into "last" and new "current" into "current"
    cursor.execute("UPDATE users SET currentLoginDate = ?, lastLoginDate = ? WHERE userID = ?", (newDate, oldDate, globalVars.userID))
    conn.commit()
