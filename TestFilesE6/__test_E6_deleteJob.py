import unittest
from unittest.mock import patch
from jobFunctions import *

class TestDeleteJobPoster(unittest.TestCase):

    @patch('builtins.input', side_effect=['2'])  # Input a job ID that doesn't belong to the user
    @patch('builtins.print')  # Mock the print function to capture the output

        #To check if you cannot delete a job if you don't own the job which is jobs.posterID = users.userID 
        
    def test_delete_other_user_job(self, mock_print, mock_input):
        # Set the user ID and create a job owned by another user
        user_id = 1  # Replace with your user ID
        job_id = 2  # Replace with a job ID that doesn't belong to the user
        expected_output = "You are not the owner of this job post. Please choose a job you posted to delete."

        # Call the deleteJobPoster function
        deleteJobPoster()

        # Check that the function prints the expected output
        assert expected_output in [call[0][0] for call in mock_print.call_args_list]

if __name__ == "__main__":
    unittest.main()
