from unittest.mock import patch
import pytest
import globalVars
import time
from database import *

# Define a custom check function
def check_print(call, expected_str):
	return any(expected_str in str(arg) for arg in call[0])


def testLoginDateTrack():
	from datetime import datetime
	from UserCreateLogin import UserLogin
	testUserName_a = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()
	TestUserPass = user_data_a[2]

	
	# Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_a[0]
	globalVars.username = user_data_a[1]
	globalVars.userFirstName = user_data_a[3]
	globalVars.userLastName = user_data_a[4]
	globalVars.userSettingMarketingEmail = user_data_a[5]
	globalVars.userSettingMarketingSMS = user_data_a[6]
	globalVars.userSettingAdvertisementTargeted = user_data_a[7]
	globalVars.userSettingLanguage = user_data_a[8]
	globalVars.userMajor = user_data_a[11]
	

	user_inputs = [
		testUserName_a,	#enter username
		TestUserPass, #enter password
		"Q", #Q to quit login page
		"Q", #Q to quit program
	]

	#test function with mocked data
	with patch('builtins.input', side_effect=user_inputs):
		#with patch('builtins.print') as mock_print:
		try:
			UserLogin()
			
		except StopIteration:
			pass

	#testLoginDate only stores the current date in YYYY-MM-DD format without the time
	testLoginDate = datetime.now().strftime("%Y-%m-%d")

	cursor.execute("SELECT currentLoginDate FROM users WHERE userID = ?",(globalVars.userID,))
	loginDate = cursor.fetchone()[0][:10] #[:10] allows the loginDate to only store the first 10 characters, i.e.,YYYY-MM-DD

	# Assert that testLoginDate and loginDate are equal
	assert testLoginDate == loginDate, "\nLogin dates are not equal\n"

def testJobDelete():
	from datetime import datetime
	from jobFunctions import deleteJobPost
	testUserName_a = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()

	# Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_a[0]
	globalVars.username = user_data_a[1]
	globalVars.userFirstName = user_data_a[3]
	globalVars.userLastName = user_data_a[4]
	globalVars.userSettingMarketingEmail = user_data_a[5]
	globalVars.userSettingMarketingSMS = user_data_a[6]
	globalVars.userSettingAdvertisementTargeted = user_data_a[7]
	globalVars.userSettingLanguage = user_data_a[8]
	globalVars.userMajor = user_data_a[11]

	title="test job"
	description="test description"
	employerName="Test employer"
	location="test location"
	salary= 59000.0
	datePosted=datetime.now()
	cursor.execute("INSERT INTO jobs (posterID, jobTitle, jobDescription, employer, location, salary, posterFirstName, posterLastName, datePosted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
					(globalVars.userID, title, description, employerName, location, salary, globalVars.userFirstName, globalVars.userLastName, datePosted))
	conn.commit()

	cursor.execute("SELECT jobID FROM jobs WHERE posterID=? AND jobTitle=?", (globalVars.userID,title,))
	testJobIDDel = cursor.fetchone()[0]

	user_inputs = [
		testJobIDDel,	#enter jobID to be deleted
	]

	#test function with mocked data
	with patch('builtins.input', side_effect=user_inputs):
		try:
			deleteJobPost()
			
		except StopIteration:
			pass


	#testLoginDate only stores the current date in YYYY-MM-DD format without the time
	testJobDelDate = datetime.now().strftime("%Y-%m-%d")

	cursor.execute("SELECT dateDeleted FROM jobs WHERE posterID = ? AND jobTitle=?",(globalVars.userID, title,))
	jobDelDate = cursor.fetchone()[0][:10] #[:10] allows the loginDate to only store the first 10 characters, i.e.,YYYY-MM-DD

	# Assert that testLoginDate and loginDate are equal
	assert testJobDelDate == jobDelDate, "\nJob deletion dates are not equal\n"

	#tear down
	cursor.execute("DELETE FROM jobs WHERE posterID=? AND jobTitle=?",(globalVars.userID, title,))
	conn.commit()


def testCreateJob(): # Needs work
	from datetime import datetime
	from jobFunctions import createJob

	testUserName_a = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()

	# Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_a[0]
	globalVars.username = user_data_a[1]
	globalVars.userFirstName = user_data_a[3]
	globalVars.userLastName = user_data_a[4]
	globalVars.userSettingMarketingEmail = user_data_a[5]
	globalVars.userSettingMarketingSMS = user_data_a[6]
	globalVars.userSettingAdvertisementTargeted = user_data_a[7]
	globalVars.userSettingLanguage = user_data_a[8]
	globalVars.userMajor = user_data_a[11]

	title="test job 2"
	description="test description 2"
	employerName="Test employer 2"
	location="test location 2"
	salary= 65000.0
	user_inputs = [
		title,	#enter title to be deleted
		description, #enter description
		employerName, #enter employer's name
		location, #enter job location
		salary, #enter salary of the job
		"N", #enter "N" to quit 
	]

	#test function with mocked data
	with patch('builtins.input', side_effect=user_inputs):
		try:
			createJob()	
		except StopIteration:
			pass
	
	#testLoginDate only stores the current date in YYYY-MM-DD format without the time
	testJobCreateDate = datetime.now().strftime("%Y-%m-%d")

	cursor.execute("SELECT datePosted FROM jobs WHERE posterID = ? AND jobTitle=?",(globalVars.userID, title,))
	jobCreateDate = cursor.fetchone()[0][:10] #[:10] allows the loginDate to only store the first 10 characters, i.e.,YYYY-MM-DD

	# Assert that testLoginDate and loginDate are equal
	assert testJobCreateDate == jobCreateDate, "\nJob creation dates are not equal\n"

	#tear down
	cursor.execute("DELETE FROM jobs WHERE posterID=? AND jobTitle=?",(globalVars.userID, title,))
	conn.commit()


def testApplicantTable():
	from datetime import datetime
	from jobFunctions import jobApplication

	testUserName_a = "TestEditProfile" #test job poster
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()

	title="test job"
	description="test description"
	employerName="Test employer"
	location="test location"
	salary= 67000.0
	datePosted=datetime.now()
	cursor.execute("INSERT INTO jobs (posterID, jobTitle, jobDescription, employer, location, salary, posterFirstName, posterLastName, datePosted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
					(user_data_a[0], title, description, employerName, location, salary, user_data_a[3], user_data_a[4], datePosted))
	conn.commit()

	testUserName_b = "TestBlankProfile" #test applicant
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_b,))
	# Retrieve test user data from the database
	user_data_b = cursor.fetchone()

	# Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_b[0]
	globalVars.username = user_data_b[1]
	globalVars.userFirstName = user_data_b[3]
	globalVars.userLastName = user_data_b[4]
	globalVars.userSettingMarketingEmail = user_data_b[5]
	globalVars.userSettingMarketingSMS = user_data_b[6]
	globalVars.userSettingAdvertisementTargeted = user_data_b[7]
	globalVars.userSettingLanguage = user_data_b[8]
	globalVars.userMajor = user_data_b[11]

	gradDate="05/15/2024"
	startDate="11/25/2023"
	whyApply="Because I can lol"
	user_inputs = [
		gradDate, #enter graduation date
		startDate, #enter date you can start working
		whyApply, #enter why you want to apply
	]

	cursor.execute("SELECT jobID FROM jobs WHERE posterID=? AND jobTitle=?", (user_data_a[0],title,))
	testJobID = cursor.fetchone()[0]

	#test function with mocked data
	with patch('builtins.input', side_effect=user_inputs):
		try:
			jobApplication(testJobID)	
		except StopIteration:
			pass

	#testLoginDate only stores the current date in YYYY-MM-DD format without the time
	testJobAppliedDate = datetime.now().strftime("%Y-%m-%d")

	cursor.execute("SELECT dateApplied FROM applicant WHERE userID = ? AND jobID = ?",(globalVars.userID, testJobID,))
	jobAppliedDate = cursor.fetchone()[0][:10] #[:10] allows the loginDate to only store the first 10 characters, i.e.,YYYY-MM-DD

	# Assert that testLoginDate and loginDate are equal
	assert testJobAppliedDate == jobAppliedDate, "\nJob creation dates are not equal\n"

	#tear down
	cursor.execute("DELETE FROM jobs WHERE posterID=? AND jobTitle=?",(user_data_a[0], title,))
	cursor.execute("DELETE FROM applicant WHERE userID=? AND jobID=?",(globalVars.userID, testJobID,))
	conn.commit()


def testUnreadMessageNotifier():
	#goal of this test is to check whether a user with unread messages gets a notification upon logging
	#in indicating that they have unread messages
	
	from notifications import LoginNotificationPanel

	testUserName_a = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()
    
    # Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_a[0]
	globalVars.username = user_data_a[1]
	globalVars.userFirstName = user_data_a[3]
	globalVars.userLastName = user_data_a[4]
	globalVars.userSettingMarketingEmail = user_data_a[5]
	globalVars.userSettingMarketingSMS = user_data_a[6]
	globalVars.userSettingAdvertisementTargeted = user_data_a[7]
	globalVars.userSettingLanguage = user_data_a[8]
	globalVars.userMajor = user_data_a[11]

	testUserName_b = "TestEditProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_b,))
	# Retrieve test user data from the database
	user_data_b = cursor.fetchone()

	subject = "Test"
	message = "Testing Unread Identifier"
	cursor.execute("""INSERT INTO messages (senderUserID, recieverUserID, subject, message) VALUES (?, ?, ?, ?)""",(user_data_b[0], globalVars.userID, subject, message))
	conn.commit()

	#test function with mocked data
	with patch('builtins.print') as mock_print:
		try:
			LoginNotificationPanel()
		except StopIteration:
			pass

	# Print out all captured calls to inspect
	for call in mock_print.call_args_list:
		print(call)


	assert any(check_print(call, "messages waiting") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM messages WHERE senderUserID=? AND recieverUserID=?",(user_data_b[0], globalVars.userID,))
	conn.commit()



def testNewUserNotifier():
	from notifications import NotifyNewStudentJoin
	from datetime import datetime
	testUserName_a = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()
    
    # Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_a[0]
	globalVars.username = user_data_a[1]
	globalVars.userFirstName = user_data_a[3]
	globalVars.userLastName = user_data_a[4]
	globalVars.userSettingMarketingEmail = user_data_a[5]
	globalVars.userSettingMarketingSMS = user_data_a[6]
	globalVars.userSettingAdvertisementTargeted = user_data_a[7]
	globalVars.userSettingLanguage = user_data_a[8]
	globalVars.userMajor = user_data_a[11]

	#create a dummy test user for testing purporses
	testDummy = "testBot"
	testPassword = "Password123$"
	fName = "Test"
	lName = "Bot"
	testMajor = "Testing"
	testUniversity = "University of Testing"
	testDateCreated = datetime.now()
	cursor.execute("""INSERT INTO users (username, password, firstName, lastName, userUniversity, userMajor, currentLoginDate, createDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",(testDummy, testPassword, fName, lName, testUniversity, testMajor, testDateCreated, testDateCreated))
	conn.commit()

	#mock parameters to pass
	# get info on current user
	cursor.execute("SELECT lastLoginDate FROM users WHERE userID = ?", (globalVars.userID,))
	result = cursor.fetchone()
	lastLogin = result[0]
	#test function with mocked parameters
	with patch('builtins.print') as mock_print:
		try:
			NotifyNewStudentJoin(globalVars.userID,lastLogin)
		except StopIteration:
			pass

	# Print out all captured calls to inspect
	for call in mock_print.call_args_list:
		print(call)


	assert any(check_print(call, "joined InCollege") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM users WHERE username = ?",(testDummy,))
	conn.commit()

def testNoProfileNotifier():
	from notifications import NotifyNoProfile
	from datetime import datetime, timedelta
	testUserName_a = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()
    
    # Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_a[0]
	globalVars.username = user_data_a[1]
	globalVars.userFirstName = user_data_a[3]
	globalVars.userLastName = user_data_a[4]
	globalVars.userSettingMarketingEmail = user_data_a[5]
	globalVars.userSettingMarketingSMS = user_data_a[6]
	globalVars.userSettingAdvertisementTargeted = user_data_a[7]
	globalVars.userSettingLanguage = user_data_a[8]
	globalVars.userMajor = user_data_a[11]

	#create a dummy test user for testing purporses
	testDummy = "testBot"
	testPassword = "Password123$"
	fName = "Test"
	lName = "Bot"
	testMajor = "Testing"
	testUniversity = "University of Testing"
	testDateCreated = datetime.now()
	cursor.execute("""INSERT INTO users (username, password, firstName, lastName, userUniversity, userMajor, currentLoginDate, createDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",(testDummy, testPassword, fName, lName, testUniversity, testMajor, testDateCreated, testDateCreated))
	conn.commit()

	#test function with mocked parameters
	with patch('builtins.print') as mock_print:
		try:
			NotifyNoProfile(globalVars.userID)
		except StopIteration:
			pass

	# Print out all captured calls to inspect
	for call in mock_print.call_args_list:
		print(call)

	assert any(check_print(call, "Don't forget to create a profile") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM users WHERE username = ?",(testDummy,))
	conn.commit()

def testApplyNotifier(): # Needs work
	from notifications import NotifyNeedToApply
	from datetime import datetime, timedelta
	testUserName_a = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()
    
    # Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_a[0]
	globalVars.username = user_data_a[1]
	globalVars.userFirstName = user_data_a[3]
	globalVars.userLastName = user_data_a[4]
	globalVars.userSettingMarketingEmail = user_data_a[5]
	globalVars.userSettingMarketingSMS = user_data_a[6]
	globalVars.userSettingAdvertisementTargeted = user_data_a[7]
	globalVars.userSettingLanguage = user_data_a[8]
	globalVars.userMajor = user_data_a[11]

	testUser = "TestUser"
	applyDates = datetime.now() - timedelta(days=8)
	formattedDate = applyDates.strftime("%Y-%m-%d %H:%M:%S.%f")

	cursor.execute("INSERT INTO applicant (userID, dateApplied) VALUES (?,?)", (testUser, formattedDate,))
	conn.commit

	#test function with mocked parameters
	with patch('builtins.print') as mock_print:
		try:
			NotifyNeedToApply(testUser)
		except StopIteration:
			pass

	assert any(check_print(call, "Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM users WHERE username = ?",(testUser,))
	conn.commit()

def testNewJobNotifier():
	from notifications import NotifyAppliedJobCount
	from datetime import datetime, timedelta

	testUserName_a = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()
    
    # Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_a[0]
	globalVars.username = user_data_a[1]
	globalVars.userFirstName = user_data_a[3]
	globalVars.userLastName = user_data_a[4]
	globalVars.userSettingMarketingEmail = user_data_a[5]
	globalVars.userSettingMarketingSMS = user_data_a[6]
	globalVars.userSettingAdvertisementTargeted = user_data_a[7]
	globalVars.userSettingLanguage = user_data_a[8]
	globalVars.userMajor = user_data_a[11]

	#create a dummy test user for testing purporses
	testDummy = "testBot"
	testPassword = "Password123$"
	fName = "Test"
	lName = "Bot"
	testMajor = "Testing"
	testUniversity = "University of Testing"
	testDateCreated = datetime.now()
	cursor.execute("""INSERT INTO users (username, password, firstName, lastName, userUniversity, userMajor, currentLoginDate, createDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",(testDummy, testPassword, fName, lName, testUniversity, testMajor, testDateCreated, testDateCreated))
	conn.commit()

	#test function with mocked parameters
	with patch('builtins.print') as mock_print:
		try:
			NotifyAppliedJobCount(globalVars.userID)
		except StopIteration:
			pass

	# Print out all captured calls to inspect
	for call in mock_print.call_args_list:
		print(call)

	assert any(check_print(call, "You have currently applied for 0 jobs") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM users WHERE username = ?",(testDummy,))
	conn.commit()

def testNewJobNotifier(): # Needs work
	from notifications import NotifyNewJobPostings
	from datetime import datetime
	testUserName_a = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()
    
    # Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_a[0]
	globalVars.username = user_data_a[1]
	globalVars.userFirstName = user_data_a[3]
	globalVars.userLastName = user_data_a[4]
	globalVars.userSettingMarketingEmail = user_data_a[5]
	globalVars.userSettingMarketingSMS = user_data_a[6]
	globalVars.userSettingAdvertisementTargeted = user_data_a[7]
	globalVars.userSettingLanguage = user_data_a[8]
	globalVars.userMajor = user_data_a[11]

	#create a dummy test user for testing purporses
	testDummy = "testBot"
	testPassword = "Password123$"
	fName = "Test"
	lName = "Bot"
	testMajor = "Testing"
	testUniversity = "University of Testing"
	testDateCreated = datetime.now()
	cursor.execute("""INSERT INTO users (username, password, firstName, lastName, userUniversity, userMajor, currentLoginDate, createDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",(testDummy, testPassword, fName, lName, testUniversity, testMajor, testDateCreated, testDateCreated))
	conn.commit()

	#mock parameters to pass
	# get info on current user
	cursor.execute("SELECT lastLoginDate FROM users WHERE userID = ?", (globalVars.userID,))
	result = cursor.fetchone()
	lastLogin = result[0]

	cursor.execute("INSERT INTO jobs (jobTitle, datePosted, posterID) VALUES ('Job1', ?, 'Poster1')", (datetime.now(), ))
	conn.commit()

	#test function with mocked parameters
	with patch('builtins.print') as mock_print:
		try:
			NotifyNewJobPostings(testDummy,lastLogin)
		except StopIteration:
			pass

	# Print out all captured calls to inspect
	for call in mock_print.call_args_list:
		print(call)

	assert any(check_print(call, "A new job, Job1 has been posted") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM users WHERE username = ?",(testDummy,))
	cursor.execute("DELETE FROM jobs WHERE jobTitle = 'Job1'")
	conn.commit()

def testDeleteJobNotifier():
	from notifications import NotifyJobDeleted
	from datetime import datetime
	testUserName_a = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_a,))
	# Retrieve test user data from the database
	user_data_a = cursor.fetchone()
    
    # Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data_a[0]
	globalVars.username = user_data_a[1]
	globalVars.userFirstName = user_data_a[3]
	globalVars.userLastName = user_data_a[4]
	globalVars.userSettingMarketingEmail = user_data_a[5]
	globalVars.userSettingMarketingSMS = user_data_a[6]
	globalVars.userSettingAdvertisementTargeted = user_data_a[7]
	globalVars.userSettingLanguage = user_data_a[8]
	globalVars.userMajor = user_data_a[11]

	#create a dummy test user for testing purporses
	testDummy = "testBot"
	testPassword = "Password123$"
	fName = "Test"
	lName = "Bot"
	testMajor = "Testing"
	testUniversity = "University of Testing"
	testDateCreated = datetime.now()
	cursor.execute("""INSERT INTO users (username, password, firstName, lastName, userUniversity, userMajor, currentLoginDate, createDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",(testDummy, testPassword, fName, lName, testUniversity, testMajor, testDateCreated, testDateCreated))
	conn.commit()

	#mock parameters to pass
	# get info on current user
	cursor.execute("SELECT lastLoginDate FROM users WHERE userID = ?", (globalVars.userID,))
	result = cursor.fetchone()
	lastLogin = result[0]

	cursor.execute("INSERT INTO jobs (jobTitle, isDeleted, dateDeleted) VALUES ('DeletedJob', 1, ?)", (datetime.now(),))
	cursor.execute("INSERT INTO applicant (userID, jobID) VALUES (?, (SELECT jobID FROM jobs WHERE jobTitle = 'DeletedJob'))", (testDummy,))
	conn.commit

	#test function with mocked parameters
	with patch('builtins.print') as mock_print:
		try:
			NotifyJobDeleted(testDummy,lastLogin)
		except StopIteration:
			pass
	
	# Print out all captured calls to inspect
	for call in mock_print.call_args_list:
		print(call)

	assert any(check_print(call, 'The job "DeletedJob" that you applied for has been deleted.') for call in mock_print.call_args_list)

	cursor.execute("DELETE FROM users WHERE username = ?",(testDummy,))
	cursor.execute("DELETE FROM jobs WHERE jobTitle = 'DeletedJob'")
	conn.commit()