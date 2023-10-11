import os, sys

current_script_directory = os.path.dirname(os.path.abspath(__file__))

parent_directory = os.path.join(current_script_directory, '..')
sys.path.append(parent_directory)

import pytest
from friendFunctions import viewFriendRequests  # Replace 'your_module' with the actual module containing the function
from unittest.mock import patch, MagicMock

def mock_cursor_and_requests():
    mock_cursor = MagicMock()
    sent_requests = [
        (1, 2, 'John', 'Doe'),
        (2, 3, 'Jane', 'Smith')
    ]
    received_requests = [
        (3, 1, 'Alice', 'Johnson', 'University A', 'Major A'),
        (4, 2, 'Bob', 'Brown', 'University B', 'Major B')
    ]
    mock_cursor.fetchall.side_effect = [sent_requests, received_requests]
    return mock_cursor

def test_view_friend_requests_with_requests(caplog, capsys):
    mock_cursor = mock_cursor_and_requests

    with patch('important.cursor', mock_cursor):
        viewFriendRequests()

        captured = capsys.readouterr()

    # Assert that the captured output contains information about sent and received requests
        assert "Friend Requests Sent:" in captured.out
        assert "To User ID: 2, Name: John Doe" in captured.out
        assert "To User ID: 3, Name: Jane Smith" in captured.out

        assert "Friend Requests Received:" in captured.out
        assert "ID:        \t 1" in captured.out
        assert "Name:      \t Alice Johnson" in captured.out
        assert "University:\t UNIVERSITY A" in captured.out
        assert "Major:     \t Johnson" in captured.out

        # Assert that the user was prompted to accept or reject requests
        assert "Enter the ID of a user whose friend request you want to ACCEPT (or 'Q' to quit):" in captured.out
        assert "Enter the ID of a user whose friend request you want to REJECT (or 'Q' to to quit):" in captured.out

def test_view_friend_requests_no_requests(capsys):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.side_effect = [[], []]  # No sent or received requests

    with patch('important.cursor', mock_cursor):
        viewFriendRequests()

    captured = capsys.readouterr()

    # Assert that the captured output indicates no friend requests
    assert "You have not sent any friend requests." in captured.out
    assert "You have not received any friend requests." in captured.out
