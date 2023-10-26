import globalVars
import time
from database import *
from UI import *


def searchPostJob():
	from loginLanding import userHome
	exitInput = True
	while exitInput:
		spacer()
		header('Welcome to Job Search')
		print("(1) Show all jobs")
		print("(2)  Post a Job")
		uInput = input("Input Selection (Q to quit): ")
		#if uInput == '1':
		#	print("under construction right now")
		#	exitInput = False
		if uInput == '2':
			createJob()
		elif uInput.upper() == 'Q' or uInput == '1':
			titles = showAllJobs()
			spacer()
			if titles:
				print("Available Jobs:\n")
				for i, title in enumerate(titles, start=1):
					print(str(i)+ ".) "+ title)
			else:
				print("No Jobs available")
			
			detailInput = int(input("Please select any number to find out more details on a job: "))

			detailData = showJobDetails(detailInput)
			spacer()
			if detailData:
				print("Job Details for this Job:")
				print("Job Title: ", detailData[0])
				print("Job Description: ", detailData[1])
				print("Employer: ", detailData[2])
				print("Location: ", detailData[3])
				print("Salary: ", detailData[4])
			else:
				print("Incorrect input!")

			applyInput = int(input("Please enter 1 to apply to this job or 2 to exit: "))

			if applyInput == 1:
				print("Under construction")
				exitInput = False
			elif applyInput == 2:
				exitInput = False
			else:
				print("invalid Option. Will now exit job search")
				exitInput = False
			#break
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
	# Connecting to database
	database_path = "your_database.db"
	table_name = "jobs"
	column_name = "jobTitle"

	connection = sqlite3.connect(database_path)
	cursor = connection.cursor()

	query = f"SELECT {column_name} FROM {table_name}"

	cursor.execute(query)
	titles = [row[0] for row in cursor.fetchall()]

	cursor.close()
	connection.close()

	return titles

def showJobDetails(ID_value):
	database_path = "your_database.db"
	table_name = "jobs"
	connection = sqlite3.connect(database_path)
	cursor = connection.cursor()

	query = f"SELECT jobTitle, jobDescription, employer, location, salary FROM {table_name} WHERE jobID = ?"
	cursor.execute(query, (ID_value,))

	row_data = cursor.fetchone()

	cursor.close()
	connection.close()
	
	return row_data