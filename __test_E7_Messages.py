from unittest.mock import patch
import pytest
#import sys
import globalVars
from database import *

# Define a custom check function
def check_print(call, expected_str):
	return any(expected_str in str(arg) for arg in call[0])

def testMessageInboxLoggedLanding(capsys):
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

