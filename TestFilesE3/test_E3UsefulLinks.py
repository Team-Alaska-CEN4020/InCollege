import sys
import os

# Get the directory of the current script
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to sys.path
parent_directory = os.path.join(current_script_directory, '..')
sys.path.append(parent_directory)

from usefulLinks import *
import pytest
from io import StringIO
from unittest.mock import patch

def test_UsefulLinksOther(capsys, monkeypatch):
    # Mock user input to simulate user interaction
    user_input_values = [ 
        "2",      
        "3",            
        "4",
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
    usefulLinksMenu()

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output based on user input
    expected_output = "under construction"

    # Assert that the captured output matches the expected output
    assert expected_output in captured.out


def test_GeneralPage(capsys, monkeypatch):
    # Mock user input to simulate user interaction
    user_input_values = [
        "1", 
        "2",      
        "3",            
        "4",
        "5",      
        "6",            
        "7",
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
    usefulLinksMenu()

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output based on user input
    expected_output = "We're here to help"
    expected_output1 = "inCollege: Welcome to inCollege, the world's largest college student network with many users in many countries and territories worldwide."
    expected_output2 = "inCollege Pressroom: Stay on top of the latest news, updates, and reports"
    expected_output3 = "Under construction"

    # Assert that the captured output matches the expected output
    assert expected_output in captured.out
    assert expected_output1 in captured.out
    assert expected_output2 in captured.out
    assert expected_output3 in captured.out


def test_GeneralSignUp(capsys, monkeypatch):
    # Mock user input to simulate user interaction
    user_input_values = [
        "1", 
        "1",  
        "Claire",
        "123$Test",
        "Claire",
        "Fairchild",
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
    usefulLinksMenu()

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output based on user input
    expected_output = "Congratulations! Your account has been successfully registered."
    expected_output1 = "Welcome User!"
    
    # Assert that the captured output matches the expected output
    assert expected_output in captured.out
    assert expected_output1 in captured.out


if __name__ == '__main__':
    pytest.main()  
