import io, os, sys
current_script_directory = os.path.dirname(os.path.abspath(__file__))

parent_directory = os.path.join(current_script_directory, '..')
sys.path.append(parent_directory)

import pytest
from unittest.mock import *
from important import *
from friendFunctions import *

# Mock the 'cursor' object and 'updateFriendDisconnect' function
mock_cursor = Mock()
mock_update_friend_disconnect = Mock()

# Assuming 'cursor' and 'updateFriendDisconnect' are part of your 'your_network' module
with patch('important.cursor', mock_cursor), \
     patch('important.updateFriendDisconnect', mock_update_friend_disconnect):

    @patch('builtins.input', side_effect=['1', 'Q'])
    def test_getFriends_with_friends(self, capsys): 
        # Mock the database query result to simulate having friends
        mock_cursor.fetchall.return_value = [(1, 'John', 'Doe', 'University A', 'Major A')]

        # Call the getFriends function
        getFriends()

        # Assertions for the scenario with friends
        expected_output = "Friend ID: 1\nName: John Doe\nUniversity: University A\nMajor: Major A"
        assert "Friend ID: 1\nName: John Doe\nUniversity: University A\nMajor: Major A" in  expected_output
        

    @patch('builtins.input', side_effect=['Q'])
    def test_getFriends_without_friends(self, capsys):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        # Mock the database query result to simulate having no friends
         mock_cursor.fetchall.return_value = []

        # Call the getFriends function
         getFriends()

         output = mock_stdout.getvalue()
         assert "No one is in your network at the moment." in output
