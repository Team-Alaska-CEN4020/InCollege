import globalVars
import time
from database import *
from UI import *
from friendFunctions import *
from userSearch import *
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()  # Create a cursor object to execute SQL commands
from profileFunctions import *


def userHome():
    from landing import startupLanding

    exitInput = 0
    while exitInput == 0:
        spacer()
        header(f"Welcome {globalVars.userFirstName}!")
        print("Please select the number of the service you would like to use:")
        print("(1)  Your InCollege Profile")
        print("(2)  Search for a job / internship")
        print("(3)  Find someone you know")
        print("(4)  Learn a new skill")
        print("(5)  Show My Network")
        print("(6)  Send Friend Request")
        print("(7)  Pending Friend Requests")

        uInput = input("Input Selection (Q to quit and return): ")

        if uInput == '1':  # UI edited for Epic-5
            userProfile()
            # userSearch()
            # createProfile()
        if uInput == '2':
            searchForJob()
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
        elif uInput == 'Q' or uInput == 'q':
            exitInput = 1
            spacer()
        else:
            print("Invalid Option. Try Again")
            spacer()





#################################################### Epic-5 ####################################################
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
        createProfile()
    else:
        while True:
            spacer()
            header(f'Welcome, {globalVars.userFirstName}!')

            print("1. Display Your Profile")
            print("2. Edit Your Profile")
            print("3. Go Back")

            option = input("Select an option (1/2/3): ")

            if option == '1':
                # Display the user's profile
                displayProfile(existing_profile)
            elif option == '2':
                # Edit the user's profile
                editProfile(existing_profile)
            elif option == '3':
                # Go back to the main menu
                break
            else:
                print("Invalid option. Please choose a valid option.")
                

      #VISIT profileFunctions FOR MORE FUNCTIONS#

#################################################### Epic-5^#####################################################


# Option functions to fill out once we understand what we need to do for them
def searchForJob():
    # print("Searching for a job is under construction")
    spacer()
    header('Welcome to Job Search')
    print("(1)  Post a Job")
    uInput = input("Input Selection (Q to quit): ")

    exitInput = 0
    while exitInput == 0:
        if uInput == '1':
            print("\nEnter the following information about the job: ")
            title = input("Enter the job title: ")
            description = input("Enter the job description: ")
            employer = input("Enter the employer: ")
            location = input("Enter the location: ")
            salary = input("Enter the job's salary: ")
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")

            storeJob(title, description, employer,
                     location, salary, firstname, lastname)

        elif uInput == 'Q' or uInput == 'q':
            exitInput = 1
            spacer()

        else:
            print("Invalid Option Try again")


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


def storeJob(title, description, employer, location, salary, firstName, lastName):
    cursor.execute("SELECT COUNT(*) FROM jobs")
    job_count = cursor.fetchone()[0]

    if job_count >= globalVars.maxJobPostings:
        print("All permitted jobs have been created. Please come back later.")
        userHome()

    cursor.execute("INSERT INTO jobs (title, description, employer, location, salary, firstname, lastname) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (title, description, employer, location, salary, firstName, lastName))

    conn.commit()
    print("Job stored in database")
    userHome()
