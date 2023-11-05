from unittest.mock import patch
import pytest
import globalVars
from database import *

# Define a custom check function
def check_print(call, expected_str):
	return any(expected_str in str(arg) for arg in call[0])


def tesNewUserImprovement():
	from UserCreateLogin import createUser

	testUserName = "testDummy"
	user_inputs = [
		testUserName,	#enter username
		"Password123$",	#enter password
		"Test",	#enter first name
		"Dummy",	#enter last name
		"Testing",	#enter major
		"University of Dummies",	#enter university
		"Y",	#want to become plus user
		"Q",	#Q to quit login home page
		"Q",	#Q to exit program
	]

	#test function with mocked data
	with patch('builtins.input', side_effect=user_inputs):
		with patch('builtins.print') as mock_print:
			try:
				createUser()
			except StopIteration:
				pass

	assert any(check_print(call, "Incollege Plus Member") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM users WHERE username=?",(testUserName))
	conn.commit()

def testSendMessageStandard():
	from messageFunctions import sendMessagePrompt
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
	globalVars.userMajor = user_data_a[10]

	testUserName_b = "TestEditProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_b,))
	# Retrieve test user data from the database
	user_data_b = cursor.fetchone()
	user_inputs = [
		testUserName_b,	#enter username of friend
		"Bloop",	#enter subject
		"I am sleepy",	#enter message
		"2",	#continue
		"0",	#exit message Inbox
		"Q",	#Q to quit login home page
		"Q",	#Q to exit program
	]

	#test function with mocked data
	with patch('builtins.input', side_effect=user_inputs):
		with patch('builtins.print') as mock_print:
			try:
				friends = getFriendsList(globalVars.userID)
				sendMessagePrompt(friends)
			except StopIteration:
				pass

	assert any(check_print(call, "Message Sent") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM messages WHERE senderUserID=? AND recieverUserID=?",(globalVars.userID, user_data_b[0]))
	conn.commit()

def testSendMessagePlus():
	from messageFunctions import sendMessagePrompt
	testUserName = "testUser"
	testPassword = "Password123$"
	fName = "Test"
	lName = "User"
	testMajor = "Testing"
	testUniversity = "University of Testing"
	testTier = 1
	cursor.execute("""INSERT INTO users (username, password, firstName, lastName, userUniversity, userMajor, userTier) VALUES (?, ?, ?, ?, ?, ?, ?)""",(testUserName, testPassword, fName, lName, testUniversity, testMajor, testTier))
	conn.commit()

	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName,))
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
	globalVars.userMajor = user_data_a[10]

	testUserName_b = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_b,))
	# Retrieve test user data from the database
	user_data_b = cursor.fetchone()
	user_inputs = [
		testUserName_b, #username of receiver
		"bloop", #enter subject
		"i am tired lol", #enter message
		"2", #2 to continue
		"Q", #Q to quit login home page
		"Q", #Q to exit program
	]

	#test function with mocked data
	with patch('builtins.input', side_effect=user_inputs):
		with patch('builtins.print') as mock_print:
			try:
				friends = getFriendsList(globalVars.userID)
				sendMessagePrompt(friends)
			except StopIteration:
				pass

	assert any(check_print(call, "Message Sent") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM users WHERE userID=? AND username=?",(globalVars.userID, globalVars.username))
	cursor.execute("DELETE FROM messages WHERE senderUserID=? AND recieverUserID=?",(globalVars.userID, user_data_b[0]))
	conn.commit()