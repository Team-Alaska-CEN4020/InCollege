import sys
sys.path.append('/home/runner/InCollege/')
import pytest
#from io import StringIO
from landing import startupLanding
from UserCreateLogin import searchUser
import time
import random
import io
from unittest.mock import patch
import unittest
import sqlite3

class TestSearchUser(unittest.TestCase):

    def setUp(self):
        # Connect to an in-memory SQLite database for testing
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        # Create a test 'users' table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT,
                firstName TEXT,
                lastName TEXT
            )
        ''')
        # Insert test data
        self.cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)", ("testuser", "password123", "Samuel", "Adams"))
        self.conn.commit()

    def tearDown(self):
        # Close the database connection after each test
        self.conn.close()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_existing_user(self, mock_stdout):
        # Call the searchUser function with test input
        with patch('builtins.input', side_effect=["Samuel", "Adams", "1"]):
            searchUser()

        # Get the printed output
        printed_output = mock_stdout.getvalue().strip()

        # Check if the expected output is in the printed output
        self.assertIn("They are a part of the InCollege system", printed_output)
        self.assertIn("Username: testuser", printed_output)
        self.assertIn("First Name: Samuel", printed_output)
        self.assertIn("Last Name: Adams", printed_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_non_existing_user(self, mock_stdout):
        # Call the searchUser function with test input for a non-existing user
        with patch('builtins.input', side_effect=["John", "Doe", "1"]):
            searchUser()

        # Get the printed output
        printed_output = mock_stdout.getvalue().strip()

        # Check if the expected output is in the printed output
        self.assertIn("They are not yet a part of the InCollege system yet", printed_output)

if __name__ == '__main__':
    unittest.main()  
"""
def test_SearchUserFound(capsys, monkeypatch):
    # Generate a random name that is in the database
    random_name = "Sam Smith"  # Modify this for your needs

    # Mock user input to simulate entering the random name
    monkeypatch.setattr("builtins.input", lambda _: random_name)

    # Capture the printed output
    with capsys.disabled():  # Disable capturing for this part
        searchUser()

    captured = capsys.readouterr()

    # Define the expected output
    expected_output = "They are a part of the InCollege system"

    # Assert that the captured output contains the expected output
    assert expected_output in captured.out, f"Expected: '{expected_output}' in output"

    # Mock user input to simulate entering "1" when prompted
    monkeypatch.setattr("builtins.input", lambda prompt: "1" if "Enter 1 to return to main menu:" in prompt else "")

    # Capture the printed output after entering "1"
    with capsys.disabled():
        searchUser()

    captured = capsys.readouterr()

    # Define the expected output after entering "1"
    expected_output = "Welcome to inCollege: inCollege is your"

    # Assert that the captured output contains the expected output
    assert expected_output in captured.out, f"Expected: '{expected_output}' in output"

def test_SearchUserNotFound(capsys, monkeypatch):
    # Generate a random name that is not in the database
    random_name = "Random Name"  # Modify this for your needs

    # Mock user input to simulate entering the random name
    monkeypatch.setattr("builtins.input", lambda _: random_name)

    # Capture the printed output
    with capsys.disabled():  # Disable capturing for this part
        searchUser()

    captured = capsys.readouterr()

    # Define the expected output
    expected_output = "They are not yet a part of the InCollege system yet"

    # Assert that the captured output contains the expected output
    assert expected_output in captured.out, f"Expected: '{expected_output}' in output"

    # Mock user input to simulate entering "1" when prompted
    monkeypatch.setattr("builtins.input", lambda prompt: "1" if "Enter 1 to return to main menu:" in prompt else "")

    # Capture the printed output after entering "1"
    with capsys.disabled():
        searchUser()

    captured = capsys.readouterr()

    # Define the expected output after entering "1"
    expected_output = "Welcome to inCollege: inCollege is your"

    # Assert that the captured output contains the expected output
    assert expected_output in captured.out, f"Expected: '{expected_output}' in output"
"""