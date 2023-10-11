import os, sys

current_script_directory = os.path.dirname(os.path.abspath(__file__))

parent_directory = os.path.join(current_script_directory, '..')
sys.path.append(parent_directory)

import pytest
import unittest
from unittest.mock import patch
from io import StringIO
from important import Languages

def mock_environment():
    with patch('important.globalVars.userSettingLanguage', 0), \
         patch('important.globalVars.isLoggedIn', True), \
         patch('important.cursor'), \
         patch('important.conn'):
        yield

def test_change_language_spanish_logged_in():
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
         patch('important.globalVars.isLoggedIn', True), \
         patch('important.globalVars.userSettingLanguage', 1), \
         patch('builtins.input', side_effect=['N']):
        Languages()

        output = mock_stdout.getvalue()

        assert "Your current language is set to Spanish" in output
        assert "Only English and Spanish are supported at this time." in output

def test_change_language_english_logged_in():
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
         patch('important.globalVars.isLoggedIn', True), \
         patch('important.globalVars.userSettingLanguage', 0), \
         patch('builtins.input', side_effect=['N']):
        Languages()

        output = mock_stdout.getvalue()

        assert "Your current language is set to English" in output
        assert "Only English and Spanish are supported at this time." in output

def test_change_language_not_logged_in():
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
         patch('important.globalVars.isLoggedIn', False), \
         patch('important.globalVars.userSettingLanguage', 0), \
         patch('builtins.input', side_effect=['N']):
        Languages()

        output = mock_stdout.getvalue()

        assert "You need to be logged in to do that" in output

def test_not_logged_in():
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
         patch('important.globalVars.isLoggedIn', False), \
         patch('builtins.input', side_effect=['N']):
        Languages()

        output = mock_stdout.getvalue()

        assert "You need to be logged in to do that" in output
