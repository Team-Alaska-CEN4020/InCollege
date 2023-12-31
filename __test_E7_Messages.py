from unittest.mock import patch
import pytest
import globalVars
from database import *

# Define a custom check function
def check_print(call, expected_str):
	return any(expected_str in str(arg) for arg in call[0])



def testMessageInboxLoggedLanding():
	#goal of this test is to check whether the message inbox option exists in the user logged in home page

	from loginLanding import userHome
	testUsername = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUsername,))
	# Retrieve test user data from the database
	user_data = cursor.fetchone()
    
    # Update the global user variables and settings
	globalVars.isLoggedIn = True
	globalVars.userID = user_data[0]
	globalVars.username = user_data[1]
	globalVars.userFirstName = user_data[3]
	globalVars.userLastName = user_data[4]
	globalVars.userSettingMarketingEmail = user_data[5]
	globalVars.userSettingMarketingSMS = user_data[6]
	globalVars.userSettingAdvertisementTargeted = user_data[7]
	globalVars.userSettingLanguage = user_data[8]
	globalVars.userMajor = user_data[11]

	user_inputs = [
		"Q",	#enter Q to quit and return to main menu
		"Q",	#enter Q to exit
	]

	#test function with mocked data
	with patch('builtins.input', side_effect=user_inputs):
		with patch('builtins.print') as mock_print:
			try:
				userHome()
			except StopIteration:
				pass

	# Print out all captured calls to inspect
	for call in mock_print.call_args_list:
		print(call)


	assert any(check_print(call, "Message Inbox") for call in mock_print.call_args_list)


def testMessageInboxHasMessages():
	#goal of this test is to check whether a user with messages is able to see their inbox
	#and able to choose a message they want to

	from messageFunctions import messageInbox
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

	user_inputs = [
		"2",	#enter 2 to continue
		"0",	#enter 0 to exit
	]

	#test function with mocked data
	with patch('builtins.input', side_effect=user_inputs):
		with patch('builtins.print') as mock_print:
			try:
				messageInbox(globalVars.userID)
			except StopIteration:
				pass

	assert any(check_print(call, "Sender") for call in mock_print.call_args_list)
	assert any(check_print(call, "Subject") for call in mock_print.call_args_list)
	
	#tear down
	cursor.execute("DELETE FROM messages WHERE senderUserID=? AND recieverUserID=?",(user_data_b[0], globalVars.userID,))
	conn.commit()


def testMessageInboxEmpty():
	#the goal of this function is to check whether the program reacts when the inbox is empty
	from messageFunctions import messageInbox
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

	user_inputs = [
		"2",	#enter 2 to continue
	]

	#test function with mocked data
	with patch('builtins.input', side_effect=user_inputs):
		with patch('builtins.print') as mock_print:
			try:
				messageInbox(globalVars.userID)
			except StopIteration:
				pass
	
	assert any(check_print(call, "inbox is currently empty") for call in mock_print.call_args_list)

def testMessageReply():
	#the goal of this function is how whether program allows user to reply to messages from either friends or plus member they
	#are not connected with
	from messageFunctions import replyMessagePrompt
	testUserName = "testBot"
	testPassword = "Password123$"
	fName = "Test"
	lName = "Bot"
	testMajor = "Testing"
	testUniversity = "University of Testing"
	cursor.execute("""INSERT INTO users (username, password, firstName, lastName, userUniversity, userMajor) VALUES (?, ?, ?, ?, ?, ?)""",(testUserName, testPassword, fName, lName, testUniversity, testMajor))
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
	globalVars.userMajor = user_data_a[11]

	testUserName_b = "TestBlankProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_b,))
	# Retrieve test user data from the database
	user_data_b = cursor.fetchone()

	subject = "whatever"
	message= "im almost done"
	cursor.execute("""INSERT INTO messages (senderUserID, recieverUserID, subject, message) VALUES (?, ?, ?, ?)""",(user_data_a[0], user_data_b[0], subject, message))
	conn.commit()

	user_inputs = [
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
				replyMessagePrompt(user_data_b[0])
			except StopIteration:
				pass

	assert any(check_print(call, "Message Sent") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM users WHERE userID=? AND username=?",(globalVars.userID, globalVars.username))
	cursor.execute("DELETE FROM messages WHERE senderUserID=? AND recieverUserID=?",(user_data_a[0], user_data_b[0]))
	cursor.execute("DELETE FROM messages WHERE senderUserID=? AND recieverUserID=?",(user_data_b[0], user_data_a[0]))
	conn.commit()


def tesNewUserImprovement():
	#the goal of this function is to test whether the program provides new users to 
	#be either a plus or standard member
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
	#the goal of this function is to test whether the program lets standard users to 
	#send messages
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
	globalVars.userMajor = user_data_a[11]

	testUserName_b = "TestEditProfile"
	cursor.execute("SELECT * FROM users WHERE username=?", (testUserName_b,))
	# Retrieve test user data from the database
	user_data_b = cursor.fetchone()

	#make the the two users friends for the sake of the function
	friendshipStat = 1
	cursor.execute("""INSERT INTO friends (userID, friendUserID, friendshipStatus) VALUES (?, ?, ?)""",(user_data_a[0], user_data_b[0], friendshipStat))
	cursor.execute("""INSERT INTO friends (userID, friendUserID, friendshipStatus) VALUES (?, ?, ?)""",(user_data_b[0], user_data_a[0], friendshipStat))
	conn.commit()

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

	#tear down messages
	cursor.execute("DELETE FROM messages WHERE senderUserID=? AND recieverUserID=?",(globalVars.userID, user_data_b[0]))
	#tear down friends
	cursor.execute("DELETE FROM friends WHERE userID=? AND friendUserID=?",(user_data_a[0], user_data_b[0]))
	cursor.execute("DELETE FROM friends WHERE userID=? AND friendUserID=?",(user_data_b[0], user_data_a[0]))
	conn.commit()


def testSendMessagePlus():
	#the goal of this function is to test whether the program lets plus users to 
	#send messages
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
	globalVars.userMajor = user_data_a[11]

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

