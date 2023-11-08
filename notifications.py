import globalVars
from database import *

def LoginNotificationPanel():
    from messageFunctions import checkUnreadStatusLogin
    print("TODO: here is where all the notifications needed for the login landing will go")
    
    # get info on current user
    user = globalVars.userID
    cursor.execute("SELECT lastLoginDate FROM users WHERE userID = ?", (user))
    result = cursor.fetchone()
    lastLogin = result[0]

    # call notifications
    NotifyNeedToApply(user)
    NotifyNoProfile(user)
    checkUnreadStatusLogin(user)
    NotifyNewStudentJoin(user, lastLogin)


def JobsNotificationPanel():
    print("TODO: here is where all the job section related notifcations will go")
    NotifyAppliedJobCount()
    NotifyNewJobPostings()
    NotifyJobDeleted()

def NotifyNeedToApply():
    print("TODO: alerts at login that its been >7days since user's last application")
    print("Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")

def NotifyNoProfile():
    print("TODO: alerts at login that user has no profile")
    print("Don't forget to create a profile")

def NotifyUnreadMessage():
    print("TODO: alert at login that user has an unread message")
    print("You have messages waiting for you")

def NotifyNewStudentJoin():
    print("TODO: alert at login with a list of new student have joined since last login")
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

#we dont need this anymore after discussing that there will be no page of notifications, 
#they will simply show up at login or at arrival to jobs section
def ViewYourNotifications():
    NotifyNeedToApply()
    print("\n")
    NotifyNoProfile()
    print("\n")
    NotifyUnreadMessage()
    print("\n")
    NotifyNewStudentJoin()
    print("\n")
    NotifyAppliedJobCount()
    print("\n")
    NotifyNewJobPostings()
    print("\n")
    NotifyJobDeleted()
    print("\n")