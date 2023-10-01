import pytest
from io import StringIO
from landing import startupLanding
from userStories import videoPlay
import time 

def test_videolink(capsys, monkeypatch):
    # Mock user input to simulate selecting option number 5
    monkeypatch.setattr("builtins.input", lambda _: "5")

    # Start the videoPlay function in a separate thread
    import threading
    video_thread = threading.Thread(target=videoPlay)
    video_thread.start()

    # Allow some time for the videoPlay function to run (3 seconds in this case)
    time.sleep(3)

    # Join the videoPlay thread to wait for it to complete
    video_thread.join()

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output
    expected_output = "Video is now playing"

    # Assert that the captured output contains the expected output
    assert expected_output in captured.out

if __name__ == '__main__':
    pytest.main()
