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
	globalVars.userMajor = user_data[10]

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


def testUnreadMessageNotifier():
	#goal of this test is to check whether a user with unread messages gets a notification upon logging
	#in indicating that they have unread messages
	
	from loginLanding import userHome

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

	subject = "Test"
	message = "Testing Unread Identifier"
	cursor.execute("""INSERT INTO messages (senderUserID, recieverUserID, subject, message) VALUES (?, ?, ?, ?)""",(user_data_b[0], globalVars.userID, subject, message))
	conn.commit()

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


	assert any(check_print(call, "unread message") for call in mock_print.call_args_list)

	#tear down
	cursor.execute("DELETE FROM messages WHERE senderUserID=? AND recieverUserID=?",(user_data_b[0], globalVars.userID,))
	conn.commit()

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
	globalVars.userMajor = user_data_a[10]

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
	globalVars.userMajor = user_data_a[10]

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

