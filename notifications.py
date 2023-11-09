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
    print("")

def JobsNotificationPanel():
    user = globalVars.userID
    cursor.execute("SELECT * FROM jobs WHERE isDeleted = 0 AND posterID = ?", (globalVars.userID))
    result = cursor.fetchone()
    #print("TODO: here is where all the job section related notifcations will go")
    NotifyAppliedJobCount()
    NotifyNewJobPostings()
    NotifyJobDeleted(user)
    #send_notification()

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


def check_deleted_jobs():
    # Retrieve the list of job applications for the user
    cursor.execute("SELECT jobID FROM applicant WHERE userID = ?", (globalVars.userID))
    jobData = cursor.fetchall()
    for job in jobData:
        # Check if the job has been deleted in the jobs table
        cursor.execute("SELECT title, is_deleted FROM jobs WHERE jobID = ?", job)
        job_info = cursor.fetchone()
        if job_info and job_info[1] == 1:
            # Job is deleted, send a notification
            job_title = job_info[0]
            print(f"A job that you applied for has been deleted: {job_title}")
            #send_notification(globalVars.userID, job_title)

'''
# Function to send a notification (you can customize this based on your notification method)
def send_notification(user_id, job_title):
    message = f"A job that you applied for has been deleted: {job_title}"
    # Use your preferred notification method here (e.g., email, SMS, push notification)

def deleteJobPost():
	cursor.execute("SELECT * FROM jobs WHERE isDeleted = 0 AND posterID = ?", (globalVars.userID,))
	jobData = cursor.fetchall()
	header("Current jobs posted: ")
	for job in jobData:
		print(f"- {job[2]}. Job ID: {job[0]}")
	
	jobIDDel = input("Please enter the ID number of the job you want to delete: ") 
	cursor.execute("SELECT * FROM jobs WHERE posterID = ? AND jobID = ?", (globalVars.userID, jobIDDel))
	userPostedJob = cursor.fetchone()
	if not userPostedJob:
		print("You are not the owner of this job post. Please choose a job you posted to delete.")
		return
	deleteDate = datetime.now()
	cursor.execute("UPDATE applicant SET isDeleted = 1, dateDeleted = ? WHERE jobID = ?",(deleteDate, jobIDDel,))
	conn.commit()

	cursor.execute("UPDATE jobs SET isDeleted = 1, dateDeleted = ? WHERE jobID = ?", (deleteDate, jobIDDel,))
	conn.commit()

	cursor.execute("UPDATE savedJobs SET isDeleted = 1, dateDeleted = ? WHERE jobID = ?", (deleteDate, jobIDDel,))
	conn.commit()
	print("The job post has been deleted. ")
'''