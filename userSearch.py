import time
from UI import *
from database import *

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
            print() # build and replace with userSearchUni
        elif uInput == '3':
            print() # build and replace with userSearchMajor
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
    
    cursor.execute("SELECT userID, firstName, LastName FROM users WHERE firstName=? AND lastName=?",(firstName, lastName))
    user = cursor.fetchone()
    
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