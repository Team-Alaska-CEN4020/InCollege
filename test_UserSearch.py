import sys
import os

# Get the directory of the current script
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to sys.path
parent_directory = os.path.join(current_script_directory, '..')
sys.path.append(parent_directory)

import pytest
from io import StringIO
from UserCreateLogin import searchUser
from unittest.mock import patch

def test_UserExists(capsys, monkeypatch):
    # Mock user input to simulate user interaction
    user_input_values = [
        "Samuel",  # Enter a first name
        "Adams",      # Enter a last name
        "1",            # Enter 1 to return
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
    searchUser()

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output based on user input
    expected_output = "They are a part of the InCollege system"

    # Assert that the captured output matches the expected output
    assert expected_output in captured.out

def test_UserNotFound(capsys, monkeypatch):
    # Mock user input to simulate user interaction
    user_input_values = [
        "John",  # Enter a first name
        "Ambrose",      # Enter a last name 
        "1",            # Enter 1 to return 
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
    searchUser()

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output based on user input
    expected_output = "They are not yet a part ofthe InCollege system yet"

    # Assert that the captured output matches the expected output
    assert expected_output in captured.out

if __name__ == '__main__':
    pytest.main()  
