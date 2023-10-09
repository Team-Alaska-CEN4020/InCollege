import pytest
import unittest
from unittest.mock import patch
from io import StringIO
import os, sys
import sqlite3
from userSearch import *

current_script_directory = os.path.dirname(os.path.abspath(__file__))

parent_directory = os.path.join(current_script_directory, '..')
sys.path.append(parent_directory)

def test_user_search_name(monkeypatch, capsys):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
        patch('important.globalVars.isLoggedIn', True), \
        patch('important.globalVars.userID', 2):

        monkeypatch.setattr('builtins.input', lambda x: 'John' if 'first name' in x else 'Doe' if 'last name' in x else '')
        userSearchName()

        output = mock_stdout.getvalue()

        assert "John Doe is an inCollege member!" in output


def test_user_search_name_none(monkeypatch, capsys):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        monkeypatch.setattr('builtins.input', lambda x: 'test' if 'first name' in x else 'testy' if 'last name' in x else '')
        userSearchName()

        output = mock_stdout.getvalue()

        assert "They are not yet an inCollege member." in output

def test_user_search_uni(monkeypatch, capsys):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
        patch('important.globalVars.isLoggedIn', True), \
        patch('important.globalVars.userID', 2):
        # Mock user input
        monkeypatch.setattr('builtins.input', lambda x: 'FSU' if 'acronym' in x else 'N' if 'potential friends' in x else '')

        # Call the function
        userSearchUni()

        # Capture printed output
        output = mock_stdout.getvalue()
        
        # Perform assertions on the captured output to check if the function behaved as expected
        assert "Search Results" in output
        assert "══════════════" in output 
        assert "Results Found:  1\n\n" in output
        assert "ID:        \t 3" in output
        assert "First Name:\t Manan" in output
        assert "Last Name: \t Ahuja" in output
        assert "Major:     \t Computer science" in output
        

def test_user_search_uni_none(monkeypatch, capsys):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Mock user input
        monkeypatch.setattr('builtins.input', lambda x: 'LSU' if 'acronym' in x else 'N' if 'potential friends' in x else '')

        # Call the function
        userSearchUni()

        # Capture printed output
        output = mock_stdout.getvalue()

        # Perform assertions on the captured output to check if the function behaved as expected
        assert "Search Results" in output
        assert "══════════════" in output 
        assert "Results Found:  0\n\n" in output

def test_user_search_major(monkeypatch, capsys):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        monkeypatch.setattr('builtins.input', lambda x: 'computer engineering' if 'major' in x else 'N' if 'potential friends' in x else '')

        # Call the function
        userSearchMajor()

        # Capture printed output
        output = mock_stdout.getvalue()

        assert "Search Results" in output
        assert "══════════════" in output 
        assert "Results Found:  1\n\n" in output
        assert "ID:        \t 2" in output
        assert "First Name:\t Sam" in output
        assert "Last Name: \t Adams" in output
        assert "University: \t USF" in output

def test_user_search_major_none(monkeypatch, capsys):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        monkeypatch.setattr('builtins.input', lambda x: 'computers' if 'major' in x else 'N' if 'potential friends' in x else '')

        # Call the function
        userSearchMajor()

        # Capture printed output
        output = mock_stdout.getvalue()

        assert "Search Results" in output
        assert "══════════════" in output 
        assert "Results Found:  0\n\n" in output

def test_user_search_friend(monkeypatch, capsys):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
        patch('important.globalVars.isLoggedIn', True), \
        patch('important.globalVars.userID', 2):

        monkeypatch.setattr('builtins.input', lambda x: 'FSU' if 'acronym' in x else 'N' if 'potential friends' in x else '')

        # Call the function
        userSearchUni()

        # Capture printed output
        output = mock_stdout.getvalue()
        
        # Perform assertions on the captured output to check if the function behaved as expected
        assert "Search Results" in output
        assert "══════════════" in output 
        assert "Results Found:  1\n\n" in output
        assert "ID:        \t 3" in output
        assert "First Name:\t Manan" in output
        assert "Last Name: \t Ahuja" in output
        assert "Major:     \t Computer science" in output
        
        monkeypatch.setattr('builtins.input', lambda x: '2')
        userSearchUni()

        updated_output = mock_stdout.getvalue()

        assert "Invalid ID selected. No friend request sent.\n" in updated_output

def test_user_search_major_friend(monkeypatch, capsys):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
        patch('important.globalVars.isLoggedIn', True), \
        patch('important.globalVars.userID', 2):
        monkeypatch.setattr('builtins.input', lambda x: 'computer engineering')

        # Call the function
        userSearchMajor()

        monkeypatch.setattr('builtins.input', lambda x: '2')
        userSearchMajor()

        updated_output = mock_stdout.getvalue()

        assert "Search Results" in updated_output
        assert "══════════════" in updated_output 
        assert "Results Found:  0\n\n" in updated_output
        assert "Invalid input. Please enter a valid user ID or 'N' to skip.\n" in updated_output


##########
# friend test functions        
##########

import pytest
from unittest.mock import patch
import io, os, sys
from important import *
from friendFunctions import *

# Mock the 'cursor' object and 'updateFriendDisconnect' function
mock_cursor = Mock()
mock_update_friend_disconnect = Mock()

# Assuming 'cursor' and 'updateFriendDisconnect' are part of your 'your_network' module
with patch('your_network.cursor', mock_cursor), \
     patch('your_network.updateFriendDisconnect', mock_update_friend_disconnect):

    @patch('builtins.input', side_effect=['1', 'Q'])
    def test_getFriends_with_friends(self, mock_input):
        # Mock the database query result to simulate having friends
        mock_cursor.fetchall.return_value = [(1, 'John', 'Doe', 'University A', 'Major A')]

        # Call the getFriends function
        getFriends()

        # Assertions for the scenario with friends
        expected_output = "Friend ID: 1\nName: John Doe\nUniversity: University A\nMajor: Major A"
        self.assertEqual(mock_update_friend_disconnect.call_count, 1)  # Ensure updateFriendDisconnect is called once
        self.assertIn(expected_output, self.stdout.getvalue())  # Capture the printed output and check for the expected content

    @patch('builtins.input', side_effect=['Q'])
    def test_getFriends_without_friends(self, mock_input):
        # Mock the database query result to simulate having no friends
        mock_cursor.fetchall.return_value = []

        # Call the getFriends function
        getFriends()

        # Assertions for the scenario without friends
        self.assertEqual(mock_update_friend_disconnect.call_count, 0)  # Ensure updateFriendDisconnect is not called
        self.assertIn("No one is in your network at the moment.", self.stdout.getvalue())  # Check for the expected message

    @patch('builtins.input', side_effect=['Q'])
    @patch('your_network.cursor', side_effect=Exception("Database error"))
    def test_getFriends_database_error(self, mock_cursor, mock_input):
        # Call the getFriends function
        getFriends()

        # Assertions for the database error scenario
        self.assertEqual(mock_update_friend_disconnect.call_count, 0)  # Ensure updateFriendDisconnect is not called
        self.assertIn("Error occurred while fetching friends:", self.stdout.getvalue())  # Check for the expected error message
