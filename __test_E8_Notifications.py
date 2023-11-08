from unittest.mock import patch
import pytest
import globalVars
from database import *



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