import os

import pytest
from jobFunctions import createJob  # Import the function to be tested

# Define test cases
def test_posting_10_jobs():
    # Simulate posting 10 jobs
    for i in range(10):
        createJob()

    # After posting 10 jobs, any additional job posting should not be allowed
    with pytest.raises(SystemExit):
        createJob()

if __name__ == "__main__":
    pytest.main()


