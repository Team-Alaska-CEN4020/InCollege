import sys
sys.path.append('/home/runner/InCollege/')
import pytest
import os
from landing import startupLanding
from UserCreateLogin import *
from userStories import *
from io import StringIO


def test_createUser(capsys, monkeypatch):
    # Mock user input to simulate user interaction
    user_input_values = [
        "SecondUser",  # Enter a unique account name
        "Valid@Pas1",      # Enter a valid password
        "John",            # Enter a first name
        "Wick",             # Enter a last name
    ]

    def mock_input(prompt):
    # Check if there are remaining values in the list
      if user_input_values:
        # Check if the next value is not an existing username or user
        next_value = user_input_values[0]
        if not username_or_user_already_exists(next_value):
            # If it's not an existing username or user, pop the next value
            return user_input_values.pop(0)
    
    # If the list is empty or the next value is an existing username or user, return None (or any other appropriate value)
    return None

    # Set the mock_input function for user input
    monkeypatch.setattr("builtins.input", mock_input)

    # Call the createUser function to collect user information
    createUser()

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output based on user input
    expected_output = "User account created successfully."

    # Assert that the captured output matches the expected output
    assert expected_output in captured.out

if __name__ == '__main__':
    pytest.main()


# def test_NewUserCreation(capsys, monkeypatch):
#     # Mock user input to simulate selecting option number 5
#     monkeypatch.setattr("builtins.input", lambda _: "2")

#     # Start the videoPlay function in a separate thread
#     import threading
#     video_thread = threading.Thread(target=videoPlay)
#     video_thread.start()

#     # Allow some time for the videoPlay function to run (3 seconds in this case)
#     time.sleep(3)

#     # Join the videoPlay thread to wait for it to complete
#     video_thread.join()

#     # Capture the printed output
#     captured = capsys.readouterr()

#     # Define the expected output
#     expected_output = "Video is now playing"

#     # Assert that the captured output contains the expected output
#     assert expected_output in captured.out

# if __name__ == '__main__':
#     pytest.main()
