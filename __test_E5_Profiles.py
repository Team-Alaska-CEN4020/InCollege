from unittest.mock import patch
import random
import pytest
import sys
from database import *

def testProfileDetails(capsys):
    from profileFunctions import displayProfile
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
    
    # test function with mocked data
    displayProfile()

    # check for headers in print out
    captured = capsys.readouterr()
    assert all(keyword in captured.out for keyword in ["Title", "Major", "University", "About", "Experience", "Education"])

def testProfileCreationGeneralDetails(capsys):
    # Function needed for testing
    from profileFunctions import createProfile

    # Simulate a logged in user with no profile
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

    # Test that it asks for all required details
    user_inputs = [
        "Software Engineer",            # enter your title
        "Y",                            # Would you like to continue? (Y/N)
        "CoMpuTeR SCiEnCe",             # Please enter your major (ALSO TESTS FORMATTING)
        "Y",                            # Would you like to continue? (Y/N)
        "UniVerSity oF SouTH FloRida",  # Please enter your university (ALSO TESTS FORMATTING)
        "Y",                            # Would you like to continue? (Y/N)
        "I love coding.",               # About yourself
        "Y",                            # Would you like to continue? (Y/N)
        "Backend Developer",            # Job title
        "Google",                       # Employer
        "01/01/2020",                   # Date started
        "12/31/2024",                   # Date ended
        "Tampa",                        # Location
        "Developed APIs",               # Job description
        "no",                           # Add more work experience?
        "Y",                            # Would you like to continue? (Y/N)
        "Harvard",                      # School name
        "Masters",                      # Degree
        "2018-2022",                    # Years attended
        "no",                           # Add more education?
        "1",                            # Return to menu
        "1",                            # Display all information
    ]

    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            try:
                createProfile()
            except StopIteration:
                pass

    # Print out all captured calls to inspect
    for call in mock_print.call_args_list:
        print(call)

    # Define a custom check function
    def check_print(call, expected_str):
        return any(expected_str in str(arg) for arg in call[0])

    # Checking for title
    assert any(check_print(call, "Title: Software Engineer") for call in mock_print.call_args_list)

    # Checking for major and re-formatting
    assert any(check_print(call, "Major: Computer Science") for call in mock_print.call_args_list)

    # Checking for university and re-formatting
    assert any(check_print(call, "University: University Of South Florida") for call in mock_print.call_args_list)

    # Checking for about
    assert any(check_print(call, "About: I love coding.") for call in mock_print.call_args_list)

    # Checking for experience
    assert any(check_print(call, "Experience:") for call in mock_print.call_args_list)
    assert any(check_print(call, "Job Title:") and check_print(call, "Backend Developer") for call in mock_print.call_args_list)
    assert any(check_print(call, "Google") for call in mock_print.call_args_list)
    assert any(check_print(call, "01/01/2020") for call in mock_print.call_args_list)
    assert any(check_print(call, "12/31/2024") for call in mock_print.call_args_list)  
    assert any(check_print(call, "Tampa") for call in mock_print.call_args_list)          
    assert any(check_print(call, "Developed APIs") for call in mock_print.call_args_list)

    # Checking for education
    assert any(check_print(call, "Education:") for call in mock_print.call_args_list)
    assert any(check_print(call, "Harvard") for call in mock_print.call_args_list)
    assert any(check_print(call, "Masters") for call in mock_print.call_args_list)
    assert any(check_print(call, "2018-2022") for call in mock_print.call_args_list)

    # Tear down test data
    # Delete from profiles table
    cursor.execute("DELETE FROM profiles WHERE userID=?", (globalVars.userID,))
    
    # Delete from education table
    cursor.execute("DELETE FROM education WHERE userID=?", (globalVars.userID,))
    
    # Delete from experience table
    cursor.execute("DELETE FROM experience WHERE userID=?", (globalVars.userID,))
    
    # Commit changes
    conn.commit()

@pytest.fixture(scope='function')
def setup_user():
    from profileFunctions import createProfile
    testUsername = "TestBlankProfile"
    cursor.execute("SELECT * FROM users WHERE username=?", (testUsername,))
    user_data = cursor.fetchone()

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
        "Software Engineer",            # enter your title
        "Y",                            # Would you like to continue? (Y/N)
        "CoMpuTeR SCiEnCe",             # Please enter your major (ALSO TESTS FORMATTING)
        "Y",                            # Would you like to continue? (Y/N)
        "UniVerSity oF SouTH FloRida",  # Please enter your university (ALSO TESTS FORMATTING)
        "Y",                            # Would you like to continue? (Y/N)
        "I love coding.",               # About yourself
        "Y",                            # Would you like to continue? (Y/N)
        "Backend Developer",            # Job title
        "Google",                       # Employer
        "01/01/2020",                   # Date started
        "12/31/2024",                   # Date ended
        "Tampa",                        # Location
        "Developed APIs",               # Job description
        "no",                           # Add more work experience?
        "Y",                            # Would you like to continue? (Y/N)
        "Harvard",                      # School name
        "Masters",                      # Degree
        "2018-2022",                    # Years attended
        "no",                           # Add more education?
        "1",                            # Return to menu
        "1",                            # Display all information
    ]

    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            try:
                createProfile()
            except StopIteration:
                pass

    yield mock_print

    # Tear down
    cursor.execute("DELETE FROM profiles WHERE userID=?", (globalVars.userID,))
    cursor.execute("DELETE FROM education WHERE userID=?", (globalVars.userID,))
    cursor.execute("DELETE FROM experience WHERE userID=?", (globalVars.userID,))
    conn.commit()

def check_print(call, expected_str):
    return any(expected_str in str(arg) for arg in call[0])

# Now for each individual test
def test_title(setup_user):
    mock_print = setup_user
    assert any(check_print(call, "Title: Software Engineer") for call in mock_print.call_args_list)

def test_major_formatting(setup_user):
    mock_print = setup_user
    assert any(check_print(call, "Major: Computer Science") for call in mock_print.call_args_list)

def test_university_formatting(setup_user):
    mock_print = setup_user
    assert any(check_print(call, "University: University Of South Florida") for call in mock_print.call_args_list)

def test_about(setup_user):
    mock_print = setup_user
    assert any(check_print(call, "About: I love coding.") for call in mock_print.call_args_list)

def test_experience(setup_user):
    mock_print = setup_user
    assert any(check_print(call, "Experience:") for call in mock_print.call_args_list)
    assert any(check_print(call, "Job Title:") and check_print(call, "Backend Developer") for call in mock_print.call_args_list)
    assert any(check_print(call, "Google") for call in mock_print.call_args_list)
    assert any(check_print(call, "01/01/2020") for call in mock_print.call_args_list)
    assert any(check_print(call, "12/31/2024") for call in mock_print.call_args_list)  
    assert any(check_print(call, "Tampa") for call in mock_print.call_args_list)          
    assert any(check_print(call, "Developed APIs") for call in mock_print.call_args_list)

def test_education(setup_user):
    mock_print = setup_user
    assert any(check_print(call, "Education:") for call in mock_print.call_args_list)
    assert any(check_print(call, "Harvard") for call in mock_print.call_args_list)
    assert any(check_print(call, "Masters") for call in mock_print.call_args_list)
    assert any(check_print(call, "2018-2022") for call in mock_print.call_args_list)

def testProfileEditDetails(capsys):
    from profileFunctions import editProfile
    # get a user object to simulate a logged in user
    # for testing, we are using username "Jay" from the database
    testUsername = "TestEditProfile"
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
    
    randNum = random.randint(1000,9999)
    print(f"Generated Random Number: {randNum}")
    user_inputs = [
        f"Tester Profile Title {randNum}",  # Enter your updated title
        f"Tester Major {randNum}",          # Enter your updated major
        f"Tester University {randNum}",     # Enter your updated major
        f"Testing about myself {randNum}",  # Enter an updated paragraph about yourself
        "no",                               # Do you want to update experience
        "no",                               # Do you want to update education
        "1"
    ]
    # test function with mocked data
    with patch('builtins.input', side_effect=user_inputs):
            try:
                editProfile()
            except StopIteration:
                pass

    # Check title
    cursor.execute("SELECT title FROM profiles WHERE userID=?", (globalVars.userID,))
    updated_title = cursor.fetchone()[0]
    assert updated_title == f"Tester Profile Title {randNum}", f"Expected title not found in the database. Got: {updated_title}"

    # Check major
    cursor.execute("SELECT major FROM profiles WHERE userID=?", (globalVars.userID,))
    updated_major = cursor.fetchone()[0]
    assert updated_major == f"Tester Major {randNum}", f"Expected major not found in the database. Got: {updated_major}"

    # Check university
    cursor.execute("SELECT university FROM profiles WHERE userID=?", (globalVars.userID,))
    updated_university = cursor.fetchone()[0]
    assert updated_university == f"Tester University {randNum}", f"Expected university not found in the database. Got: {updated_university}"

    # Check paragraph/about
    cursor.execute("SELECT About FROM profiles WHERE userID=?", (globalVars.userID,))
    updated_about = cursor.fetchone()[0]
    assert updated_about == f"Testing about myself {randNum}", f"Expected paragraph not found in the database. Got: {updated_about}"