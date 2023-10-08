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
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
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
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Mock user input
        monkeypatch.setattr('builtins.input', lambda x: 'FSU' if 'acronym' in x else 'N' if 'potential friends' in x else '')

        # Call the function
        userSearchUni()

        # Capture printed output
        output = mock_stdout.getvalue()
        print(output)

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
