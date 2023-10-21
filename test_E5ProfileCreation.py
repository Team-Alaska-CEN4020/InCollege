import pytest
from profileFunctions import displayProfile
from database import *

# get a user object to simulate a logged in user
# for testing, we are using username "Jay" from the database
testUsername = "Jay"
cursor.execute("SELECT * FROM users WHERE username=?", (testUsername,))
# Retrieve user data from the database
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
    
# create a profile object to pass based on above user.
cursor.execute("SELECT * FROM profiles WHERE userID = ?",(globalVars.userID,))
existing_profile = cursor.fetchone()

def test_entity(capsys):
    # get a user object to simulate a logged in user
    # for testing, we are using username "Jay" from the database
    testUsername = "Jay"
    cursor.execute("SELECT * FROM users WHERE username=?", (testUsername,))
    # Retrieve user data from the database
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
    
    # create a profile object to pass based on above user.
    cursor.execute("SELECT * FROM profiles WHERE userID = ?",
                   (globalVars.userID,))
    existing_profile = cursor.fetchone()

    displayProfile(existing_profile)

    captured = capsys.readouterr()
    assert all(keyword in captured.out for keyword in ["Title", "Major", "University", "About", "Experience", "Education"])