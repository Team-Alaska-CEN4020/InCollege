import globalVars
from jobFunctions import createJob, searchPostJob
import pytest
from unittest.mock import patch
from io import StringIO

# Mock user input
@pytest.fixture
def mock_input(monkeypatch):
    user_inputs = ["1", "0", "Q"]
    user_input_index = 0

    def mock_user_input(prompt):
        nonlocal user_input_index
        print(prompt, end="")
        user_input = user_inputs[user_input_index]
        user_input_index += 1
        return user_input

    monkeypatch.setattr("builtins.input", mock_user_input)

# Mock database connection
@pytest.fixture
def mock_database_connection(monkeypatch):
    with patch("jobFunctions.connection") as connection:
        connection.cursor.return_value.__enter__.return_value.__exit__.return_value = None
        yield connection

# Mock showAllJobs
def mock_showAllJobs():
    return ["Job Title 1", "Job Title 2"]

# Mock showJobDetails
def mock_showJobDetails(input):
    return ("Job Title", "Job Description", "Employer", "Location", 50000.0)

def test_search_post_job(mock_input, mock_database_connection):
    with patch("jobFunctions.showAllJobs", new=mock_showAllJobs), \
         patch("jobFunctions.showJobDetails", new=mock_showJobDetails):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            searchPostJob()

            output = mock_stdout.getvalue()
            assert "Job Title 1" in output
            assert "Job Title 2" in output
            assert "Job Title: Job Title" in output
            assert "Job Description: Job Description" in output
            assert "Employer: Employer" in output
            assert "Location: Location" in output
            assert "Salary: 50000.0" in output
            assert "Please enter 1 to apply" in output

