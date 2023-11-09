import globalVars
import time
from database import *
from UI import *
from datetime import datetime
#from notifications import JobsNotificationPanel

#header("Here's a quick look at what you missed!")
#JobsNotificationPanel()

def searchPostJob():
	from loginLanding import userHome
	exitInput = True
	while exitInput:
		spacer()
		header('Welcome to Job Search')
		print("(1) Show all jobs")
		print("(2) Post a Job")
		print("(3) Jobs Applied To")
		print("(4) Jobs Not Applied To")
		print("(5) Jobs Saved")
		print("(6) Delete a job post. ")

		uInput = input("Input Selection (Q to quit): ")
		if  uInput == '1':
			showJobApply()

		elif uInput == '2':
			createJob()

		elif uInput == '3':
			spacer()
			applications(globalVars.userID)
			time.sleep(5)

		elif uInput == '4':
			spacer()
			missingJobTitles = noApplications(globalVars.userID)
			
			if missingJobTitles:
				print(f"Jobs that you have not not applied to!:\n{missingJobTitles}")
			else:
				print(f"You have applied to all jobs!")
			time.sleep(5)

		elif uInput == '5':
			spacer()
			print("Displaying all Saved Jobs:")
			displaySavedJobs(globalVars.userID)

			djInput = input("Please enter a job title you would like to delete or enter 0 to exit: ")
			if djInput != '0':
				deleteJob(globalVars.userID, djInput)
			else:
				print("Invalid Option. Exiting job search")

		elif uInput == '6':
			deleteJobPost()
			time.sleep(2)

		elif uInput == 'Q':
			exitInput = False
		else:
			print("Invalid Option. Try again")
			time.sleep(2)


def createJob():
	loopBreaker = True
	while loopBreaker: 
		spacer()
		cursor.execute("SELECT COUNT(jobID) FROM jobs")
		job_count = cursor.fetchone()[0]
	
		print(f"JobID count : {job_count}")
		if job_count >= globalVars.maxJobPostings:
			print("All permitted jobs have been created. Please come back later.")
			#searchPostJob()
			time.sleep(2)
			return
	

		title = input("Enter the title of of your job: ")
		description = input("Enter a description of the job: ")
		employerName = input("Enter the name of the company for the job: ")
		location = input("Enter the location for the job: ")
		salary = float(input("Enter the yearly salary for the job: "))
		datePosted = datetime.now()

		cursor.execute("INSERT INTO jobs (posterID, jobTitle, jobDescription, employer, location, salary, posterFirstName, posterLastName, datePosted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
					(globalVars.userID, title, description, employerName, location, salary, globalVars.userFirstName, globalVars.userLastName, datePosted))
		conn.commit()

		print("Your job has been posted to the job Board!")
		continuePosting = input("Would you like to post more jobs? (Y/N): ")
		if continuePosting.upper() != 'Y':
			loopBreaker = False
		else: 
			continue

#this functions allows users to delete a job they they posted
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

def showAllJobs():
	query = f"SELECT jobID, jobTitle FROM jobs WHERE isDeleted = 0"

	cursor.execute(query)
	titles = cursor.fetchall()

	return titles


def showJobApply():
	menuLooper = True
	while menuLooper:
		jobData = showAllJobs()
		spacer()
		if jobData:
			print("Available Jobs:\n")
			for job in jobData:
				print(f"- {job[1]}. Job ID: {job[0]}")
		else:
			print("No Jobs available")
		
		detailInput = int(input("Please select the job ID number to find out more details on the job or input 0 to quit: "))

		if detailInput != 0:
			detailData = showJobDetails(detailInput)
			spacer()
			if detailData:
				print("Job Details for this Job:")
				print("Job Title: ", detailData[1])
				print("Job Description: ", detailData[2])
				print("Employer: ", detailData[3])
				print("Location: ", detailData[4])
				print("Salary: ", detailData[5])

				applyInput = int(input("Please enter 1 to apply to this job, 2 to save Job or 3 to exit: "))
				if applyInput == 1:
					jobApplication(detailData[0])
					return
				elif applyInput == 2:
					spacer()
					print("Saving job!")
					saveJob(globalVars.userID, detailData[0], detailData[1])
					time.sleep(2)
					return
				elif applyInput == 3:
					return
				else:
					print("Invalid Option. Will now exit job search")

		elif detailInput == 0:
			menuLooper = False
		else:
			print("Invalid Option.")
			menuLooper = False


#this function allows users to apply to jobs
def jobApplication(job_ID):
	cursor.execute("SELECT userID FROM applicant WHERE userID = ? AND jobID = ?", (globalVars.userID, job_ID))
	applied_already = cursor.fetchone()
	cursor.execute("SELECT posterID FROM jobs WHERE posterID = ? AND jobID = ?", (globalVars.userID, job_ID))
	userPostedJob = cursor.fetchone()
	if applied_already:
		print("You have already applied for this job. Please choose a different job.")
		time.sleep(2)
		return
	if userPostedJob:
		print("You cannot apply for a job you posted. Please choose a different job.")
		time.sleep(2)
		return
	counter1 = True
	while counter1:
		gradDate = input("Please enter your graduation date (mm/dd/yyyy): ")
		if is_valid_date(gradDate):
			break
		else: 
			print("Please enter your graduation date in the correct format (mm/dd/yyyy).")
	counter2 = True
	while counter2:
		startDate = input("Please enter the date you can start working for this position (mm/dd/yyyy): ")
		if is_valid_date(startDate):
			break
		else: 
			print("Please enter your starting date in the correct format (mm/dd/yyyy).")
	whyApply = input("Provide a paragraph explaining why you think that you would be a great fit for this position: ")
	applicationDate = datetime.now()
	cursor.execute("INSERT INTO applicant (userID, jobID, firstName, lastName, gradDate, startDate, paragraph, dateApplied) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
					(globalVars.userID, job_ID, globalVars.userFirstName, globalVars.userLastName, gradDate, startDate, whyApply, applicationDate))
	conn.commit()

	print("Job has been successfully applied to!")
	time.sleep(2)


#checks whether the entered date is in the correct format (mm/dd/yyyy)
def is_valid_date(input_string):
    try:
        # Attempt to parse the input string as a date with the format "mm/dd/yyyy"
        datetime.strptime(input_string, "%m/%d/%Y")
        return True  # Input string is a valid date in the required format
    except ValueError:
        return False  # Input string is not in the required format


def showJobDetails(ID_value):
	query = f"SELECT jobID, jobTitle, jobDescription, employer, location, salary FROM jobs WHERE jobID = ?"
	cursor.execute(query, (ID_value,))

	row_data = cursor.fetchone()

	return row_data

def saveJob(user_ID, job_ID, job_Title): 
	cursor.execute("SELECT COUNT(jobTitle) FROM savedJobs WHERE userID = ? AND jobID = ?",(user_ID, job_ID,))
	result = cursor.fetchone()
	job_count = result[0]

	if job_count > 0:
		print("You already have this job saved!")
		time.sleep(3)
		return
	else:
		cursor.execute("INSERT INTO savedJobs (userID, jobID, jobTitle) VALUES (?, ?, ?)", (user_ID, job_ID, job_Title))
		conn.commit()

def displaySavedJobs(user_ID):
	cursor.execute('SELECT jobTitle FROM savedJobs WHERE userID = ? and isDeleted = 0', (user_ID,))
	saved_jobs = cursor.fetchall()
	if saved_jobs:
		for i, title in enumerate(saved_jobs, start=1):
			print(f"{i}.) Job Title: {title[0]}")
	else:
		print("No saved jobs found for this user.")
	return saved_jobs

def deleteJob(user_id, jobTitle):
	cursor.execute('DELETE FROM savedJobs WHERE userID = ? and jobTitle = ?', (user_id, jobTitle))
	conn.commit()

def applications(user_id):
	query = """
			SELECT jobs.jobTitle
			FROM applicant
			INNER JOIN jobs ON applicant.jobID = jobs.jobID
			WHERE applicant.userID = ? AND applicant.isDeleted = 0"""
	cursor.execute(query, (user_id,))
	conn.commit()

	allJobsApps = [row[0] for row in cursor.fetchall()]

	if allJobsApps:
		formatted_list = "\n".join([f"{i+1}.) {job_id}" for i, job_id in enumerate(allJobsApps)])
		print(f"Jobs that you have applied to!\n{formatted_list}")

def noApplications(user_id):
	query = """
			SELECT jobs.jobTitle
			FROM jobs
			WHERE jobs.jobID NOT IN (
				SELECT applicant.jobID
				FROM applicant
				WHERE applicant.userID = ?
			) AND jobs.jobID IN (
				SELECT jobID
				FROM jobs
			) AND jobs.isDeleted = 0
		"""
	
	cursor.execute(query, (user_id,))

	missing_jobTitles = [row[0] for row in cursor.fetchall()]

	formatted_list = "\n".join(f"{i + 1}.) {title}" for i, title in enumerate(missing_jobTitles))
	return formatted_list
