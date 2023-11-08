import globalVars
import time
from database import *
from UI import *
from friendFunctions import *
from userSearch import *
from jobFunctions import *
from profileFunctions import createProfile, displayProfile, editProfile
from messageFunctions import *
from notifications import *

#conn = sqlite3.connect('your_database.db')
#cursor = conn.cursor()  # Create a cursor object to execute SQL commands

def userHome():
    exitInput = 0
    while exitInput == 0:
        #commenting out as functionality has been replalced in epic 8
        #cursor.execute("SELECT * FROM deletedJobApplicants WHERE userID = ?", (globalVars.userID,))
        #userIDApplicationDel = cursor.fetchone()
        #if userIDApplicationDel:
        #    print("A job you applied for has been deleted. ")
        #    cursor.execute("DELETE FROM deletedJobApplicants WHERE userID = ?", (globalVars.userID,))
        #    conn.commit()
        #    time.sleep(3)
            
        spacer()
        checkUnreadStatusLogin(globalVars.userID)
        
        header(f"Welcome {globalVars.userFirstName}!")

        print("Here's a quick look at what you missed!")
        ViewYourNotifications()

        print("Please select the number of the service you would like to use:")
        print("(1)  Your InCollege Profile")
        print("(2)  Search for a job / internship")
        print("(3)  Find someone you know")
        print("(4)  Learn a new skill")
        print("(5)  Show My Network")
        print("(6)  Send Friend Request")
        print("(7)  Pending Friend Requests")
        print("(8)  Message Inbox")
        

        uInput = input("Input Selection (Q to quit and return): ")

        if uInput == '1':  
            # UI edited for Epic-5
            userProfile()
        elif uInput == '2':
            searchPostJob()
        elif uInput == '3':
            userSearch()
        elif uInput == '4':
            learnASkill()
        elif uInput == '5':
            getFriends()
        elif uInput == '6':
            userSearch()
        elif uInput == '7':
            viewFriendRequests()
        elif uInput == '8':
            messageInbox(globalVars.userID)
        elif uInput == '9':
            ViewYourNotifications()
        elif uInput.upper() == 'Q':
            exitInput=1
            spacer()
        else:
            print("Invalid Option. Try Again")
            spacer()




# Function to create a User Profile as a new user or existing user
def userProfile():
    # Check if a profile exists for the logged-in user in the profiles table
    cursor.execute("SELECT * FROM profiles WHERE userID = ?",
                   (globalVars.userID,))
    existing_profile = cursor.fetchone()

    # Check if an experience exists for the logged-in user in the experience table
    cursor.execute("SELECT * FROM experience WHERE userID = ?",
                   (globalVars.userID,))
    experience_existing = cursor.fetchone()

    # Check if an education exists for the logged-in user in the education table
    cursor.execute("SELECT * FROM education WHERE userID = ?",
                   (globalVars.userID,))
    education_existing = cursor.fetchone()

    if (not existing_profile) or (not experience_existing) or (not education_existing):
        # If no profile exists, create one
        #If no education or experience exists then users get to continue from where they left off
        createProfile()
    else:
        menuLooper = True
        while menuLooper:
            spacer()
            header(f'Welcome, {globalVars.userFirstName}!')

            print("1. Display Your Profile")
            print("2. Edit Your Profile")
            print("3. Go Back")

            option = input("Select an option (1/2/3): ")

            if option == '1':
                # Display the user's profile
                displayProfile()
            elif option == '2':
                # Edit the user's profile
                editProfile()
            elif option == '3':
                # Go back to the main menu
                menuLooper = False
            else:
                print("Invalid option. Please choose a valid option.")
                

      #VISIT profileFunctions FOR MORE FUNCTIONS#


def learnASkill():
    loopBreaker1 = True
    while loopBreaker1:
        print("\nPlease select any of following skills:")
        print("1. Web Development ")
        print("2. Leadership ")
        print("3. Time management ")
        print("4. Data Literacy ")
        print("5. Interview Prep ")
        print("6. Return to Welcome Screen ")
        UserOption = int(input("Please select your option: "))
        if UserOption == 1:
            print("Web Development is under construction")
        elif UserOption == 2:
            print("Leadership is under construction")
        elif UserOption == 3:
            print("Time management is under construction")
        elif UserOption == 4:
            print("Data literacy is under construction")
        elif UserOption == 5:
            print("Interview prep is under construction")
        elif UserOption == 6:
            userHome()
        else:
            print("Invalid input.")

        cont = input("Would you like to continue (yes/no): ")
        if cont.lower() == "yes":
            continue
        elif cont.lower() != "yes":
            loopBreaker1 = False
            exit(0)