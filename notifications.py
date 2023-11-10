import globalVars
from UI import *
from database import *
from datetime import datetime, timedelta
from jobFunctions import *

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

def JobsNotificationPanel():

    header("Here's a quick look at what you missed!")

    user = globalVars.userID
    cursor.execute("SELECT * FROM jobs WHERE isDeleted = 0 AND posterID = ?", (user,))
    result = cursor.fetchone()
    lastLogin = result[0]

    # call notificaions
    NotifyAppliedJobCount(user)
    NotifyNewJobPostings(user, lastLogin)
    NotifyJobDeleted(user, lastLogin)

    # UI padding
    print("")
    header("                                       ")

def NotifyNeedToApply(user):
    try:
        #set application age limit
        appAgeMax = 7

        #get latest apply date for user
        cursor.execute("SELECT dateApplied FROM applicant WHERE userID = ? ORDER BY dateApplied DESC LIMIT 1", (user,))
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
                time.sleep(1)
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
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")

def NotifyNewStudentJoin(user, lastLogin):
    cursor.execute("SELECT firstName, lastName FROM users WHERE createDate > ? AND userID <> ?", (lastLogin, user,))
    newUsers = cursor.fetchall()

    if newUsers:
        for user in newUsers:
            print(f"{user[0]} {user[1]} has joined InCollege")
            time.sleep(1)
    else:
        return None

def NotifyAppliedJobCount(user):
    # given a userID, just print how many jobs they have applied for
    
    #query and store the count of jobs for the given user
    cursor.execute("SELECT COUNT(jobID) AS jobCount FROM applicant WHERE isDeleted = 0 AND userID = ?", (user,))
    jobCount = cursor.fetchone()

    #print the amount of jobs user applied for
    print(f"You have currently applied for {jobCount[0]} jobs")
    time.sleep(1)

def NotifyNewJobPostings(user, lastLogin):
    # given a userID and last login date, this should print out all the jobs posted since last login
    # I have the user ID as an input
    # I have the lastLogin also as an input

    # query all jobs and filter out the ones posted after last login. Only need the job titles
    cursor.execute("SELECT jobTitle FROM jobs WHERE isDeleted = 0 AND datePosted > ? AND posterID <> ?", (lastLogin,user,))
    newJobs = cursor.fetchall()

    # print all the jobs in the right format
    if newJobs:
        for jobs in newJobs:
            print(f"A new job, {jobs[0]} has been posted")
            time.sleep(1)
    else:
        return None
    

def NotifyJobDeleted(user, lastLogin):
    cursor.execute("SELECT jobTitle FROM jobs WHERE isDeleted = 1 AND dateDeleted > ? AND posterID <> ?", (lastLogin,user,))
    deleted_job = cursor.fetchall()

    if deleted_job:
        for jobs in deleted_job:
            print(f'The job "{jobs[0]}" that you applied for has been deleted.')
            time.sleep(1)
    else:
        return None