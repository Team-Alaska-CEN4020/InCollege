import globalVars
from UI import *
from database import *
from datetime import datetime, timedelta

def LoginNotificationPanel():
    from messageFunctions import checkUnreadStatusLogin
    
    header("Here's a quick look at what you missed!")
    
    # get info on current user
    user = globalVars.userID
    cursor.execute("SELECT lastLoginDate FROM users WHERE userID = ?", (user,))
    result = cursor.fetchone()
    lastLogin = result[0]

    # call notifications
    NotifyNeedToApply(user)
    NotifyNoProfile(user)
    checkUnreadStatusLogin(user)
    NotifyNewStudentJoin(user, lastLogin)
    
    # UI padding
    print("")
    header("                                       ")
    print("")

def JobsNotificationPanel():
    print("TODO: here is where all the job section related notifcations will go")
    NotifyAppliedJobCount()
    NotifyNewJobPostings()
    NotifyJobDeleted()

def NotifyNeedToApply(user):
    try:
        #set application age limit
        appAgeMax = 7

        #get latest apply date for user
        cursor.execute("SELECT dateApplied FROM applicant WHERE userID = ? ORDER BY dateApplied DESC LIMIT 1", (user))
        result = cursor.fetchone()

        #check if there even is a latest date
        if result is None:
            return None
        else:
            #if there is then generate and format a date to compare against latest apply date
            today = datetime.now()
            appDateMax = today + timedelta(days=appAgeMax)
            formattedDate = appDateMax.strftime("%Y-%m-%d %H:%M:%S.%f")

            #check dates to see if latest apply date is older than appAgeMax
            if dateCompare(formattedDate, result[0]) == 1:
                print("Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
            else:
                return None
            
    except Exception as e:
        print(f"An error occurred: {e}")

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
    cursor.execute("SELECT firstName, lastName FROM users WHERE createDate > ? AND userID <> ?", (lastLogin, user,))
    newUsers = cursor.fetchall()

    if newUsers:
        for user in newUsers:
            print(f"{user[0]} {user[1]} has joined InCollege")
    else:
        return None

def NotifyAppliedJobCount():
    print("TODO: when in the jobs section, user sees below message with x replaced with actual number")
    print("You have currently applied for x jobs")

def NotifyNewJobPostings():
    print("TODO: when in the jobs section, see a list of all new postings since last logged in")
    print("A new job <job title> has been posted.")

def NotifyJobDeleted():
    print("TODO: when in the jobs section, user sees any jobs that have been deleted since last login")
    print("A job that you applied for has been deleted <Job Title>")
