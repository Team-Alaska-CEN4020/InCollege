import pytest
from unittest.mock import patch
from jobFunctions import jobApplication
from database import cursor, conn
import globalVars
import sqlite3
import random

# Mock the database connection
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()


def test_job_application_successful():
    # Configure user and select a random job for the test (job ID from 1 to 4)
    job_ID = 4
    globalVars.userID = 7

    with patch('builtins.input', side_effect=['01/01/2024', '01/01/2024', 'I am a great fit for this job']):
        with patch('builtins.print') as mock_print:
            jobApplication(job_ID)

    # Check that the function printed the appropriate message
    assert "Job has been successfully applied to!" in [call[0][0] for call in mock_print.call_args_list]


def test_job_application_already_applied():
    # Set up the database with a sample job and user
    job_ID = 4
    globalVars.userID = 1
    
    with patch('builtins.input', side_effect=['01/01/2024', '01/01/2024', 'I am a great fit for this job']):
        with patch('builtins.print') as mock_print:
            jobApplication(job_ID)
    
    # Check that the function printed the appropriate message
    assert "Job has been successfully applied to!" in [call[0][0] for call in mock_print.call_args_list]




# Cleanup database resources after the tests
def cleanup():
    # Clean up the database by removing the sample data
    cursor.execute("DELETE FROM applicant WHERE userID = '7'")
    cursor.execute("DELETE FROM savedJobs WHERE userID = '7'")
    conn.commit()

# Include other tests and necessary setup/teardown code

# Ensure cleanup is called after all tests
def pytest_sessionfinish(session, exitstatus):
    cleanup()
    cursor.close()
    conn.close()

