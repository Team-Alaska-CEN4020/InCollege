from database import *
from UI import *
import time
from friendFunctions import *
from networks import * 
#intialize a stack to navigate through the program 
#navigation_stack = []

def userHome():
    from landing import startupLanding
  
    exitInput = 0 
    while exitInput == 0:
        header("Welcome User!")
        print("Please select the number of the service you would like to use:")
        print("(1)  Search for a job / internship")
        print("(2)  Find someone that they know")
        print("(3)  Learn a new skill")
        print("(4)  Show My Network")
        print("(5)  Send Friend Request")
        print("(6)  Pending Friend Requests")
    
        uInput = input("Input Selection (Q to quit and return): ")
      
        if uInput == '1':
          searchForJob()
        elif uInput == '2':
          findSomeoneTheyKnow()
        elif uInput == '3':
          learnASkill()
        elif uInput == '4':
          showMyNetwork()
        elif uInput == '5':
          sendFriendRequest()
        elif uInput == '6':
          viewFriendRequests()
        elif uInput == 'Q' or 'q':
          exitInput = 1
          spacer() 
        else:
            print("Invalid Option. Try Again")
            spacer()

# Option functions to fill out once we understand what we need to do for them 
def searchForJob():
    #print("Searching for a job is under construction")
    print("\nWelcome to Job Search!\n1) post a job\n2) go back to the previous page")
    choice = int(input("Please select an option: "))
  
    if(choice == 1):
      print("\nEnter the following information about the job: ")
      title = input("Enter the job title: ")
      description = input("Enter the job description: ")
      employer = input("Enter the employer: ")
      location = input("Enter the location: ")
      salary = input("Enter the job's salary: ")
      firstname = input("Enter your first name: ")
      lastname = input("Enter your last name: ")

      storeJob(title, description, employer, location, salary, firstname, lastname)

      
    elif(choice == 2):
      print("returning to job search")
      userHome()
    else:
      while(choice!= 1 and choice != 2):
        print("invalid input")
        print("1) post a job\n2) go back to the previous page")
        choice = input("Please select an option: ")

  
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
        elif cont.lower()!="yes":
            loopBreaker1=False
            exit(0)


def storeJob(title, description, employer, location, salary, firstName, lastName):
  cursor.execute("SELECT COUNT(*) FROM jobs")
  job_count = cursor.fetchone()[0]

  if job_count >= MAX_ACCOUNTS:
    print("All permitted jobs have been created. Please come back later.")
    userHome()

  cursor.execute("INSERT INTO jobs (title, description, employer, location, salary, firstname, lastname) VALUES (?, ?, ?, ?, ?, ?, ?)", (title, description, employer, location, salary, firstName, lastName))
  
  conn.commit()
  print("Job stored in database")
  userHome()


def findSomeoneTheyKnow():
    #firstname = input("\nEnter a first name to search: ")
    lastname = input("Enter a last name: ")
    major = input("Enter their major: ")
    university = input("Enter their University: ")
    
    cursor.execute("SELECT * FROM users WHERE lastName=? OR major=? OR university=?  ",(lastname , major , university))
    user = cursor.fetchone()
    
    loopBreaker = True
    loopBreak = True
  
    if user:
        while loopBreaker:
            print("They are a part of the InCollege system")
            print("Username" + user[1])
            print("Last Name" + user[3])
            print("Major: "  + user[8])
            print("Last Name: " + user[9])
        
            loopBreaker = False
            time.sleep(3)
            userHome()
    
    else:
        print("They are not yet a part ofthe InCollege system yet")  
        while loopBreak:
            uInput = input("Enter 1 to return to main menu: ")
            if uInput == "1":
                loopBreak = False
                userHome()
            else:
                uInput = input("Enter 1 to return to main menu please: ")
                userHome()

