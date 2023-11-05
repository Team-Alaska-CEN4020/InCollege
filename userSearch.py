import time
import globalVars
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
    #do not use .capitalize(), it converts a last name such as BlankProfile to Blankprofile
    
    cursor.execute("SELECT userID, firstName, lastName FROM users WHERE firstName=? AND lastName=? AND isDeleted=0",(firstName, lastName))
    user = cursor.fetchone()
    print("\n")
    header('Search Results')
    if not user:
        print("They are not yet an inCollege member.")  
    else:
        foundID = user[0]
        print(firstName + " " + lastName + " is an inCollege member!")
        if globalVars.isLoggedIn == True and globalVars.userID != user[0]:
            uInput = input("Would you like to add them as a friend? (Y/N): ")
            if uInput.upper() == 'Y':
                friendRequest(foundID)
    time.sleep(3)

def userSearchUni():
    spacer()
    header('Search by University')
    uniInput = input("Enter the acronym of your University (ie. USF): ").upper()

    cursor.execute("SELECT userID, firstName, LastName, userMajor FROM users WHERE UPPER(userUniversity)=? AND userID !=? AND isDeleted=0", (uniInput,globalVars.userID))
    results = cursor.fetchall()
    print("\n")
    header('Search Results')
    print("Results Found: ", len(results))
    print("\n")

    resultIDs = {}
    for row in results:
        resultIDs[row[0]] = row
        print("ID:        \t", row[0])
        print("First Name:\t", row[1])
        print("Last Name: \t", row[2])
        print("Major:     \t", row[3].capitalize())
        print("\n")
    if globalVars.isLoggedIn:
        uInput = input("See any potential friends? Enter their ID (or type 'N' to skip): ")
        if uInput.upper() != 'N':
            try:
                selectedUserID = int(uInput)
                if selectedUserID in resultIDs:
                    friendRequest(selectedUserID)
                    print(f"Friend request sent to {resultIDs[selectedUserID][1]} {resultIDs[selectedUserID][2]}!\n")
                else:
                    print("Invalid ID selected. No friend request sent.\n")
            except ValueError:
                print("Invalid input. Please enter a valid user ID or 'N' to skip.\n")

def userSearchMajor():
    spacer()
    header('Search by Major')
    majorInput = input("Enter the name of your major: ").upper()

    cursor.execute("SELECT userID, firstName, LastName, userUniversity FROM users WHERE UPPER(userMajor)=? AND userID !=? AND isDeleted=0", (majorInput,globalVars.userID))
    results = cursor.fetchall()
    print("\n")
    header('Search Results')
    print("Results Found: ", len(results))
    print("\n")

    resultIDs = {}
    for row in results:
        resultIDs[row[0]] = row
        print("ID:        \t", row[0])
        print("First Name:\t", row[1])
        print("Last Name: \t", row[2])
        print("Univerity: \t", row[3].upper())
        print("\n")
    if globalVars.isLoggedIn:
        uInput = input("See any potential friends? Enter their ID (or type 'N' to skip): ")
        if uInput.upper() != 'N':
            try:
                selectedUserID = int(uInput)
                if selectedUserID in resultIDs:
                    friendRequest(selectedUserID)
                    print(f"Friend request sent to {resultIDs[selectedUserID][1]} {resultIDs[selectedUserID][2]}!\n")
                else:
                    print("Invalid ID selected. No friend request sent.\n")
            except ValueError:
                print("Invalid input. Please enter a valid user ID or 'N' to skip.\n")

def friendRequest(toUserID):
    print("sending friend request to ID:" + str(toUserID)) # replace with function call to DB to add request
    insertFriendRequest(globalVars.userID, toUserID)
    time.sleep(3)