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
			print("under construction right now")
			spacer()
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