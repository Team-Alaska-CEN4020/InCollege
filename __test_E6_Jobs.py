import pytest
import globalVars
import random
import unittest
from jobFunctions import createJob
from database import *

def testMaxJobListing(capsys):
    # Goal of this test is to check if the number of current stored jobs
    # and validate if it already exceeds the value set in globalVars.maxJobPostings
    
    # Get the count of current stored
    cursor.execute("SELECT COUNT(jobID) FROM jobs WHERE isDeleted=0")
    result = cursor.fetchone() #result of the query is stored as a tuple data type (basically an array)
    jobCount = result[0] #naturalize data type of tuple stored result into int jobCount
    
    # initial check if there are already 
    assert jobCount <= globalVars.maxJobPostings, f"jobCount exceeded limit of 10 with {jobCount} postings"

    # create dummy jobs until filled to max allowed
    while jobCount < globalVars.maxJobPostings:
        # posterID 7 = userID 7 which is a test user and has no valid job postings
        cursor.execute("INSERT INTO jobs (posterID) VALUES (7)")
        conn.commit() # commit changes (the insert) to db
        jobCount += 1 # increment loop control variable
    
    # now test if it will allow you to create a job when the max exists
    try:
        createJob()
    # because our app always defaults to a menu input, we have to tell the test 
    # that if it asks for an input and the test doesnt have one to give, 
    # then just continue with the test function
    except StopIteration:
        pass
    
    # capture what the application prints out for the user
    printCapture = capsys.readouterr().out

    # check if createJob() throws the max jobs error, it should pass if it does
    assert "All permitted jobs have been created. Please come back later." in printCapture

    # clean up from testing
    cursor.execute("DELETE FROM jobs WHERE posterID=7") # just the ones from the test user
    conn.commit()

def testListingAllJobsPass1(capsys):
    from jobFunctions import showAllJobs
    # test will take random valid job title from db and check if showAllJobs() displays it
    cursor.execute("SELECT jobTitle FROM jobs WHERE isDeleted = 0 ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    jobTitle = results[0]

    # try block to ignore menu input
    try:
        funcTitles = showAllJobs()
    except StopIteration:
        pass
    
    #check if the randomly pulled valid job is returned 
    assert any(title for _, title in funcTitles if title == jobTitle)

def testListingAllJobsPass2(capsys):
    from jobFunctions import showAllJobs
    # same test as above but for another pass since check is random
    # test will take random valid job title from db and check if showAllJobs() displays it
    cursor.execute("SELECT jobTitle FROM jobs WHERE isDeleted = 0 ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    jobTitle = results[0]

    # try block to ignore menu input
    try:
        funcTitles = showAllJobs()
    except StopIteration:
        pass
    
    #check if the randomly pulled valid job is returned 
    assert any(title for _, title in funcTitles if title == jobTitle)

def testListingAllJobsPass3(capsys):
    from jobFunctions import showAllJobs
    # same test as above but for another pass since check is random
    # test will take random valid job title from db and check if showAllJobs() displays it
    cursor.execute("SELECT jobTitle FROM jobs WHERE isDeleted = 0 ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    jobTitle = results[0]

    # try block to ignore menu input
    try:
        funcTitles = showAllJobs()
    except StopIteration:
        pass
    
    #check if the randomly pulled valid job is returned 
    assert any(title for _, title in funcTitles if title == jobTitle)

def testListingAllJobsPass4(capsys):
    from jobFunctions import showAllJobs
    # same test as above but for another pass since check is random
    # test will take random valid job title from db and check if showAllJobs() displays it
    cursor.execute("SELECT jobTitle FROM jobs WHERE isDeleted = 0 ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    jobTitle = results[0]

    # try block to ignore menu input
    try:
        funcTitles = showAllJobs()
    except StopIteration:
        pass
    
    #check if the randomly pulled valid job is returned 
    assert any(title for _, title in funcTitles if title == jobTitle)

def testListingAllJobsPass5(capsys):
    from jobFunctions import showAllJobs
    # same test as above but for another pass since check is random
    # test will take random valid job title from db and check if showAllJobs() displays it
    cursor.execute("SELECT jobTitle FROM jobs WHERE isDeleted = 0 ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    jobTitle = results[0]

    # try block to ignore menu input
    try:
        funcTitles = showAllJobs()
    except StopIteration:
        pass
    
    #check if the randomly pulled valid job is returned 
    assert any(title for _, title in funcTitles if title == jobTitle)

def testListingAppliedJobsPass1(capsys):
    from jobFunctions import applications
    # test will take find a job a user has applied for and then check if applications() reports it
    # applications takes in a userID, we need to find a random userID with an applied for job
    cursor.execute("SELECT userID FROM applicant ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    testUserID = results[0]

    # find all the job titles our test user is applied to
    cursor.execute(f"SELECT j.jobTitle FROM jobs j JOIN applicant a ON j.jobID = a.jobID WHERE userID = {testUserID}")
    result = cursor.fetchall()
    jobTitles = [title[0] for title in result] #unpack tuple into array

    # call application(user_id)
    try:
        applications(testUserID)
    except StopIteration: #ignore menu asking for input
        pass

    # capture printed text for analysis
    printCapture = capsys.readouterr()
    printedItems = printCapture.out.strip().split('\n')

    for jobTitle in jobTitles:
        matches = [item for item in printedItems if jobTitle in item]
        assert matches, f"Job title {jobTitle} not found in printed items"

def testListingAppliedJobsPass2(capsys):
    from jobFunctions import applications
    # same test as above but for another pass since check is random 
    # test will take find a job a user has applied for and then check if applications() reports it
    # applications takes in a userID, we need to find a random userID with an applied for job
    cursor.execute("SELECT userID FROM applicant ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    testUserID = results[0]

    # find all the job titles our test user is applied to
    cursor.execute(f"SELECT j.jobTitle FROM jobs j JOIN applicant a ON j.jobID = a.jobID WHERE userID = {testUserID}")
    result = cursor.fetchall()
    jobTitles = [title[0] for title in result] #unpack tuple into array

    # call application(user_id)
    try:
        applications(testUserID)
    except StopIteration: #ignore menu asking for input
        pass

    # capture printed text for analysis
    printCapture = capsys.readouterr()
    printedItems = printCapture.out.strip().split('\n')

    for jobTitle in jobTitles:
        matches = [item for item in printedItems if jobTitle in item]
        assert matches, f"Job title {jobTitle} not found in printed items"

def testListingAppliedJobsPass3(capsys):
    from jobFunctions import applications
    # same test as above but for another pass since check is random 
    # test will take find a job a user has applied for and then check if applications() reports it
    # applications takes in a userID, we need to find a random userID with an applied for job
    cursor.execute("SELECT userID FROM applicant ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    testUserID = results[0]

    # find all the job titles our test user is applied to
    cursor.execute(f"SELECT j.jobTitle FROM jobs j JOIN applicant a ON j.jobID = a.jobID WHERE userID = {testUserID}")
    result = cursor.fetchall()
    jobTitles = [title[0] for title in result] #unpack tuple into array

    # call application(user_id)
    try:
        applications(testUserID)
    except StopIteration: #ignore menu asking for input
        pass

    # capture printed text for analysis
    printCapture = capsys.readouterr()
    printedItems = printCapture.out.strip().split('\n')

    for jobTitle in jobTitles:
        matches = [item for item in printedItems if jobTitle in item]
        assert matches, f"Job title {jobTitle} not found in printed items"

def testListingAppliedJobsPass4(capsys):
    from jobFunctions import applications
    # same test as above but for another pass since check is random 
    # test will take find a job a user has applied for and then check if applications() reports it
    # applications takes in a userID, we need to find a random userID with an applied for job
    cursor.execute("SELECT userID FROM applicant ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    testUserID = results[0]

    # find all the job titles our test user is applied to
    cursor.execute(f"SELECT j.jobTitle FROM jobs j JOIN applicant a ON j.jobID = a.jobID WHERE userID = {testUserID}")
    result = cursor.fetchall()
    jobTitles = [title[0] for title in result] #unpack tuple into array

    # call application(user_id)
    try:
        applications(testUserID)
    except StopIteration: #ignore menu asking for input
        pass

    # capture printed text for analysis
    printCapture = capsys.readouterr()
    printedItems = printCapture.out.strip().split('\n')

    for jobTitle in jobTitles:
        matches = [item for item in printedItems if jobTitle in item]
        assert matches, f"Job title {jobTitle} not found in printed items"

def testListingAppliedJobsPass5(capsys):
    from jobFunctions import applications
    # same test as above but for another pass since check is random 
    # test will take find a job a user has applied for and then check if applications() reports it
    # applications takes in a userID, we need to find a random userID with an applied for job
    cursor.execute("SELECT userID FROM applicant ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    testUserID = results[0]

    # find all the job titles our test user is applied to
    cursor.execute(f"SELECT j.jobTitle FROM jobs j JOIN applicant a ON j.jobID = a.jobID WHERE userID = {testUserID}")
    result = cursor.fetchall()
    jobTitles = [title[0] for title in result] #unpack tuple into array

    # call application(user_id)
    try:
        applications(testUserID)
    except StopIteration: #ignore menu asking for input
        pass

    # capture printed text for analysis
    printCapture = capsys.readouterr()
    printedItems = printCapture.out.strip().split('\n')

    for jobTitle in jobTitles:
        matches = [item for item in printedItems if jobTitle in item]
        assert matches, f"Job title {jobTitle} not found in printed items"

def testListingNotAppliedJobsPass1(capsys):
    from jobFunctions import noApplications
    # test will grab a random userid from DB make a list of all jobIDs not applied for then check 
    # noApplications takes in a userID, we need to find a random userID with an applied for job
    cursor.execute("SELECT userID FROM users ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    testUserID = results[0]

    # find all the job titles our test user is not applied to
    query = """
    SELECT j.jobTitle
    FROM jobs j
    LEFT JOIN applicant a ON j.jobID = a.jobID AND a.userID = ?
    WHERE a.jobID IS NULL;
    """
    cursor.execute(query,(testUserID,))
    result = cursor.fetchall()
    jobTitles = [title[0] for title in result] #unpack tuple into array

    # call noApplication(user_id) and store returned values
    try:
        funcTitles = noApplications(testUserID)
    except StopIteration: #ignore menu asking for input
        pass

    # split funcTitles
    splitTitles = [line.split(".) ")[1] for line in funcTitles.split('\n')]

    # check each value from db is inside object returned from noApplications()
    for title in jobTitles:
        assert title in splitTitles, f"Job title {title} for userID: {testUserID} not found in returned items"

def testListingNotAppliedJobsPass2(capsys):
    from jobFunctions import noApplications
    # test will grab a random userid from DB make a list of all jobIDs not applied for then check 
    # noApplications takes in a userID, we need to find a random userID with an applied for job
    cursor.execute("SELECT userID FROM users ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    testUserID = results[0]

    # find all the job titles our test user is not applied to
    query = """
    SELECT j.jobTitle
    FROM jobs j
    LEFT JOIN applicant a ON j.jobID = a.jobID AND a.userID = ?
    WHERE a.jobID IS NULL;
    """
    cursor.execute(query,(testUserID,))
    result = cursor.fetchall()
    jobTitles = [title[0] for title in result] #unpack tuple into array

    # call noApplication(user_id) and store returned values
    try:
        funcTitles = noApplications(testUserID)
    except StopIteration: #ignore menu asking for input
        pass

    # split funcTitles
    splitTitles = [line.split(".) ")[1] for line in funcTitles.split('\n')]

    # check each value from db is inside object returned from noApplications()
    for title in jobTitles:
        assert title in splitTitles, f"Job title {title} for userID: {testUserID} not found in returned items"

def testListingNotAppliedJobsPass3(capsys):
    from jobFunctions import noApplications
    # test will grab a random userid from DB make a list of all jobIDs not applied for then check 
    # noApplications takes in a userID, we need to find a random userID with an applied for job
    cursor.execute("SELECT userID FROM users ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    testUserID = results[0]

    # find all the job titles our test user is not applied to
    query = """
    SELECT j.jobTitle
    FROM jobs j
    LEFT JOIN applicant a ON j.jobID = a.jobID AND a.userID = ?
    WHERE a.jobID IS NULL;
    """
    cursor.execute(query,(testUserID,))
    result = cursor.fetchall()
    jobTitles = [title[0] for title in result] #unpack tuple into array

    # call noApplication(user_id) and store returned values
    try:
        funcTitles = noApplications(testUserID)
    except StopIteration: #ignore menu asking for input
        pass

    # split funcTitles
    splitTitles = [line.split(".) ")[1] for line in funcTitles.split('\n')]

    # check each value from db is inside object returned from noApplications()
    for title in jobTitles:
        assert title in splitTitles, f"Job title {title} for userID: {testUserID} not found in returned items"

def testListingNotAppliedJobsPass4(capsys):
    from jobFunctions import noApplications
    # test will grab a random userid from DB make a list of all jobIDs not applied for then check 
    # noApplications takes in a userID, we need to find a random userID with an applied for job
    cursor.execute("SELECT userID FROM users ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    testUserID = results[0]

    # find all the job titles our test user is not applied to
    query = """
    SELECT j.jobTitle
    FROM jobs j
    LEFT JOIN applicant a ON j.jobID = a.jobID AND a.userID = ?
    WHERE a.jobID IS NULL;
    """
    cursor.execute(query,(testUserID,))
    result = cursor.fetchall()
    jobTitles = [title[0] for title in result] #unpack tuple into array

    # call noApplication(user_id) and store returned values
    try:
        funcTitles = noApplications(testUserID)
    except StopIteration: #ignore menu asking for input
        pass

    # split funcTitles
    splitTitles = [line.split(".) ")[1] for line in funcTitles.split('\n')]

    # check each value from db is inside object returned from noApplications()
    for title in jobTitles:
        assert title in splitTitles, f"Job title {title} for userID: {testUserID} not found in returned items"

def testListingNotAppliedJobsPass5(capsys):
    from jobFunctions import noApplications
    # test will grab a random userid from DB make a list of all jobIDs not applied for then check 
    # noApplications takes in a userID, we need to find a random userID with an applied for job
    cursor.execute("SELECT userID FROM users ORDER BY RANDOM() LIMIT 1")
    results = cursor.fetchone()
    testUserID = results[0]

    # find all the job titles our test user is not applied to
    query = """
    SELECT j.jobTitle
    FROM jobs j
    LEFT JOIN applicant a ON j.jobID = a.jobID AND a.userID = ?
    WHERE a.jobID IS NULL;
    """
    cursor.execute(query,(testUserID,))
    result = cursor.fetchall()
    jobTitles = [title[0] for title in result] #unpack tuple into array

    # call noApplication(user_id) and store returned values
    try:
        funcTitles = noApplications(testUserID)
    except StopIteration: #ignore menu asking for input
        pass

    # split funcTitles
    splitTitles = [line.split(".) ")[1] for line in funcTitles.split('\n')]

    # check each value from db is inside object returned from noApplications()
    for title in jobTitles:
        assert title in splitTitles, f"Job title {title} for userID: {testUserID} not found in returned items"

def testSavedJobs(capsys): #in progress
    from jobFunctions import saveJob, displaySavedJobs
    # tests both saveJob() and displaySavedJobs()
    # pick random userID for testing
    cursor.execute("SELECT userID FROM users ORDER BY RANDOM() LIMIT 1")
    testUserID = cursor.fetchone()[0]

    # pick random jobID for testing
    cursor.execute("SELECT jobID, jobTitle FROM jobs ORDER BY RANDOM() LIMIT 1")
    testJobID = cursor.fetchone()[0]
    
    # create a randomized jobtitle to pass to saveJob
    randomInt = random.randint(1000,9999)
    testJobTitle = f"TEST TITLE {randomInt}"

    # check if the savedJobs row exists
    cursor.execute(f"SELECT 1 FROM savedJobs WHERE userID = {testUserID} AND jobID = {testJobID}")
    rowExists = cursor.fetchone() is not None

    # insert a new row if it doesn't exist using saveJob()
    if not rowExists:
        saveJob(testUserID, testJobID, testJobTitle)
    
    # test displaySavedJobs
    try:
        savedJobs = displaySavedJobs(testUserID)
        
        # check if testJobTitle is found in saved jobs
        assert (testJobTitle,) in savedJobs, f"Expected jobTitle '{testJobTitle}' not found for userID {testUserID}"
    
    finally:
        if not rowExists:
            cursor.execute("DELETE FROM savedJobs WHERE jobTitle = ?", (testJobTitle,))
            conn.commit()  

class TestDeleteJobPoster(unittest.TestCase):
    from unittest.mock import patch
    @patch('builtins.input', side_effect=['2'])  # Input a job ID that doesn't belong to the user
    @patch('builtins.print')  # Mock the print function to capture the output

        #To check if you cannot delete a job if you don't own the job which is jobs.posterID = users.userID 
        
    def test_delete_other_user_job(self, mock_print, mock_input):
        from jobFunctions import deleteJobPoster
        # Set the user ID and create a job owned by another user
        user_id = 1  # Replace with your user ID
        job_id = 2  # Replace with a job ID that doesn't belong to the user
        expected_output = "You are not the owner of this job post. Please choose a job you posted to delete."

        # Call the deleteJobPoster function
        deleteJobPoster()

        # Check that the function prints the expected output
        assert expected_output in [call[0][0] for call in mock_print.call_args_list]

# Test if user can successfully apply for a job

def test_job_application_successful():
    from unittest.mock import patch, call
    from jobFunctions import jobApplication
    job_ID = 4
    globalVars.userID = 7

    try:
        with patch('builtins.input', side_effect=['01/01/2024', '01/01/2024', 'I am a great fit for this job']):
            with patch('builtins.print') as mock_print:
                with patch('time.sleep', lambda _: None):
                    jobApplication(job_ID)

        # Check that the function printed the appropriate message
        mock_print.assert_any_call("Job has been successfully applied to!")

    finally:
        # local test cleanup
        cursor.execute("DELETE FROM applicant WHERE userID=7") # just the ones from the test user
        conn.commit()



# Test if user gets the correct message when they've already applied for a job
def test_job_application_already_applied():
    from unittest.mock import patch, call
    from jobFunctions import jobApplication
    job_ID = 4
    globalVars.userID = 1

    # add a test application
    try:
        with patch('builtins.input', side_effect=['01/01/2024', '01/01/2024', 'I am a great fit for this job']):
            with patch('builtins.print') as mock_print:
                jobApplication(job_ID)
    
        # now check if the function will allow the same application, it should not.
        with patch('builtins.input', side_effect=['01/01/2024', '01/01/2024', 'I am a great fit for this job']):
            with patch('builtins.print') as mock_print:
                jobApplication(job_ID)
        
        # Check that the function printed the appropriate message
        mock_print.assert_any_call("You have already applied for this job. Please choose a different job.")
    
    finally:
        # clean up DB from tests
        cursor.execute("DELETE FROM applicant WHERE userID=7") # just the ones from the test user
        conn.commit()