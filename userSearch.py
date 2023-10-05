import time
from UI import *
from database import *

foundUserID = None

def userSearch(): 
    menuLooper = True
    while menuLooper:
        spacer()
        header('Friend Search')
        print("How would you like to search for your friend?")
        print("(1)  Search by First & Last Name")
        print("(2)  Search by University")
        print("(3)  Search by Major")

        uInput = input("Input Selection (Q to quit and return): ")
        
        if uInput == '1':
            userSearchName()
        elif uInput == '2':
            userSearchUni()
        elif uInput == '3':
            userSearchMajor()
        elif uInput == 'Q' or uInput == 'q':
            menuLooper = False
        else:
            print("Incorrect Input. Please Try Again")
            time.sleep(2)

def userSearchName():
    spacer()
    header('Search By Name')
    firstName = input("\nEnter a first name to search: ")
    lastName = input("Enter a last name: ")
    
    cursor.execute("SELECT userID, firstName, LastName FROM users WHERE firstName=? AND lastName=? AND isDeleted=0",(firstName, lastName))
    user = cursor.fetchone()
    print("\n")
    header('Search Results')
    if not user:
        print("They are not yet an inCollege member.")  
    else:
        print(firstName + " " + lastName + " is an inCollege member!")
    
    if globalVars.isLoggedIn == True:
        uInput = input("Would you like to add them as a friend? (Y/N): ")
        if uInput == 'Y' or uInput == 'y':
            print("send request here")# replace with function call to DB to add request

    time.sleep(3)

def userSearchUni():
    spacer()
    header('Search by University')
    uniInput = input("Enter the acronym of your University (ie. USF): ").upper()

    cursor.execute("SELECT userID, firstName, LastName, userMajor FROM users WHERE UPPER(userUniversity)=? and isDeleted=0", (uniInput,))
    results = cursor.fetchall()
    print("\n")
    header('Search Results')
    print("Results Found: ", len(results))
    print("\n")

    for row in results:
        print("First Name:\t", row[1])
        print("Last Name: \t", row[2])
        print("Major:     \t", row[3].capitalize())
        print("\n")
    
    input("Press Enter to Continue...")

def userSearchMajor():
    spacer()
    header('Search by Major')
    majorInput = input("Enter the name of your major: ").upper()

    cursor.execute("SELECT userID, firstName, LastName, userUniversity FROM users WHERE UPPER(userMajor)=? and isDeleted=0", (majorInput,))
    results = cursor.fetchall()
    print("\n")
    header('Search Results')
    print("Results Found: ", len(results))
    print("\n")

    for row in results:
        print("First Name:\t", row[1])
        print("Last Name: \t", row[2])
        print("Univerity: \t", row[3].upper())
        print("\n")
    
    input("Press Enter to Continue...")