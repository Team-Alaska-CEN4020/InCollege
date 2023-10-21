import sys, os
currentDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)
import pytest
from landing import *
from io import StringIO

def test_display_profile_after_login(monkeypatch, capsys):
    # Simulate sequence of user inputs: "Jay", "Password123$", "1", "1"
    monkeypatch.setattr('builtins.input', lambda _: ("Jay" if not hasattr(test_display_profile_after_login, "counter") else "Password123$" if test_display_profile_after_login.counter == 1 else "1"))
    
    if not hasattr(test_display_profile_after_login, "counter"):
        test_display_profile_after_login.counter = 0  # Initialize counter
    test_display_profile_after_login.counter += 1

    startupLanding()

    captured = capsys.readouterr()
    assert all(keyword in captured.out for keyword in ["Title", "Major", "University", "About", "Experience", "Education"])