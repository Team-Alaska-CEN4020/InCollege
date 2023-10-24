import globalVars
import time
from database import *
from UI import *

def searchForJob():
    # print("Searching for a job is under construction")
    spacer()
    header('Welcome to Job Search')
    print("(1)  Post a Job")
    uInput = input("Input Selection (Q to quit): ")

    exitInput = 0
    while exitInput == 0:
        if uInput == '1':
            print("\nEnter the following information about the job: ")
            title = input("Enter the job title: ")
            description = input("Enter the job description: ")
            employer = input("Enter the employer: ")
            location = input("Enter the location: ")
            salary = input("Enter the job's salary: ")
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")

            storeJob(title, description, employer,
                     location, salary, firstname, lastname)

        elif uInput.upper() == 'Q':
            exitInput = 1
            spacer()

        else:
            print("Invalid Option Try again")


def storeJob(title, description, employer, location, salary, firstName, lastName):
	from loginLanding import userHome
	cursor.execute("SELECT COUNT(*) FROM jobs")
	job_count = cursor.fetchone()[0]
	
	if job_count >= globalVars.maxJobPostings:
		print("All permitted jobs have been created. Please come back later.")
		userHome()

	cursor.execute("INSERT INTO jobs (title, description, employer, location, salary, firstname, lastname) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (title, description, employer, location, salary, firstName, lastName))

	conn.commit()
	print("Job stored in database")
	userHome()