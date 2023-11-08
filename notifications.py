import globalVars
import time
from UI import *
from database import *

def LoginNotificationPanel():
    from messageFunctions import checkUnreadStatusLogin
    
    header("Here's a quick look at what you missed!")
    
    # get info on current user
    user = globalVars.userID
    cursor.execute("SELECT lastLoginDate FROM users WHERE userID = ?", (user,))
    result = cursor.fetchone()
    lastLogin = result[0]

    # call notifications
    #NotifyNeedToApply(user)
    #NotifyNoProfile(user)
    checkUnreadStatusLogin(user)
    #NotifyNewStudentJoin(user, lastLogin)

def JobsNotificationPanel():
    print("TODO: here is where all the job section related notifcations will go")
    NotifyAppliedJobCount()
    NotifyNewJobPostings()
    NotifyJobDeleted()

def NotifyNeedToApply(user):
    print(f"TODO: alerts at login that its been >7days since user's last application {user}")
    print("Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")

def NotifyNoProfile(user):
    # check DB if profile exists
    try:
        cursor.execute("SELECT profileID FROM profiles WHERE userid=?", (user,))
        result = cursor.fetchone()
        if result is None:
            print("Don't forget to create a profile")
    except Exception as e:
        print(f"An error occurred: {e}")

def NotifyNewStudentJoin(user, lastLogin):
    print(f"TODO: alert at login with a list of new student {user} have joined since last login {lastLogin}")
    print("<first name> <last name> x has joined InCollege")

def NotifyAppliedJobCount():
    print("TODO: when in the jobs section, user sees below message with x replaced with actual number")
    print("You have currently applied for x jobs")

def NotifyNewJobPostings():
    print("TODO: when in the jobs section, see a list of all new postings since last logged in")
    print("A new job <job title> has been posted.")

def NotifyJobDeleted():
    print("TODO: when in the jobs section, user sees any jobs that have been deleted since last login")
    print("A job that you applied for has been deleted <Job Title>")
