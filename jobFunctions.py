import globalVars
import time
from database import *
from UI import *

connection = sqlite3.connect('your_database.db')
cursor = connection.cursor()

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

		uInput = input("Input Selection (Q to quit): ")
		#if uInput == '1':
		#	print("under construction right now")
		#	exitInput = False
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

		cursor.execute("INSERT INTO jobs (posterID, jobTitle, jobDescription, employer, location, salary, posterFirstName, posterLastName) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
					(globalVars.userID, title, description, employerName, location, salary, globalVars.userFirstName, globalVars.userLastName))
		conn.commit()

		print("Your job has been posted to the job Board!")
		continuePosting = input("Would you like to post more jobs? (Y/N): ")
		if continuePosting.upper() != 'Y':
			time.sleep(2)
			loopBreaker = False
		else: 
			continue

def showAllJobs():
	query = f"SELECT jobTitle FROM jobs"

	cursor.execute(query)
	titles = [row[0] for row in cursor.fetchall()]

	return titles


def showJobApply():
	menuLooper = True
	while menuLooper:
		titles = showAllJobs()
		spacer()
		if titles:
			print("Available Jobs:\n")
			for i, title in enumerate(titles, start=1):
				print(str(i)+ ".) "+ title)
		else:
			print("No Jobs available")
		
		detailInput = int(input("Please select any number to find out more details on a job or input 0 to quit: "))

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
					print("Under construction")
					return
				elif applyInput == 2:
					spacer()
					print("Saving job!")
					saveJob(globalVars.userID, detailData[0], detailData[1])
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
		connection.commit()

def displaySavedJobs(user_ID):
	cursor.execute('SELECT jobTitle FROM savedJobs WHERE userID = ?', (user_ID,))
	saved_jobs = cursor.fetchall()
	if saved_jobs:
		for i, title in enumerate(saved_jobs, start=1):
			print(f"{i}.) Job Title: {title[0]}")
	else:
		print("No saved jobs found for this user.")
	return saved_jobs

def deleteJob(user_id, jobTitle):
	cursor.execute('DELETE FROM savedJobs WHERE userID = ? and jobTitle = ?', (user_id, jobTitle))
	connection.commit()

def applications(user_id):
	query = """
			SELECT jobs.jobTitle
			FROM applicant
			INNER JOIN jobs ON applicant.jobID = jobs.jobID
			WHERE applicant.userID = ?"""
	cursor.execute(query, (user_id,))
	connection.commit()

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
			)
		"""
	
	cursor.execute(query, (user_id,))

	missing_jobTitles = [row[0] for row in cursor.fetchall()]

	formatted_list = "\n".join(f"{i + 1}.) {title}" for i, title in enumerate(missing_jobTitles))
	return formatted_list