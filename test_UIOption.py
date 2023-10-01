import pytest
from io import StringIO
from landing import startupLanding, UserLogin
from UserCreateLogin import createUser, deleteUser, searchUser
from userStories import videoPlay
from unittest.mock import patch

# Define a mock_input function to simulate user input
def mock_input(prompt):
    if prompt == "Please select either 1, 2, 3, 4, or 5 based on which option you would like to do: ":
        return "1"  # Simulate selecting option 1 (UserLogin)
    else:
        return "5"  # Simulate selecting option 5 (videoPlay) for other cases

# Define test functions for each option
def test_return_to_startupLanding_option_1(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", mock_input)
    with patch("landing.UserLogin") as user_login_mock:
        startupLanding()
        user_login_mock.assert_called_once()

# def test_return_to_startupLanding_option_2(capsys, monkeypatch):
#     monkeypatch.setattr("builtins.input", mock_input)
#     with patch("userStories.createUser") as create_user_mock:
#         startupLanding()
#         create_user_mock.assert_called_once()

# def test_return_to_startupLanding_option_3(capsys, monkeypatch):
#     monkeypatch.setattr("builtins.input", mock_input)
#     with patch("userStories.deleteUser") as delete_user_mock:
#         startupLanding()
#         delete_user_mock.assert_called_once()

# def test_return_to_startupLanding_option_4(capsys, monkeypatch):
#     monkeypatch.setattr("builtins.input", mock_input)
#     with patch("userStories.searchUser") as search_user_mock:
#         startupLanding()
#         search_user_mock.assert_called_once()

# def test_return_to_startupLanding_option_5(capsys, monkeypatch):
#     monkeypatch.setattr("builtins.input", mock_input)
#     with patch("userStories.videoPlay") as video_play_mock:
#         startupLanding()
#         video_play_mock.assert_called_once()

if __name__ == '__main__':
    pytest.main()
