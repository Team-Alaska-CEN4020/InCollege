from database import *
from UserCreateLogin import *

# Define a function to get user information by username
def get_user_info(username):
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()
    if user_data:
        return {
            'id': user_data[0],
            'username': user_data[1],
            'firstName': user_data[2],
            'lastName': user_data[3],
            'major': user_data[4],
            'university': user_data[5],
        }
    return None

# Define a function to get username by username
def get_username_by_username(username):
    cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
    username = cursor.fetchone()
    if username:
        return username[0]
    return None

# Define a function to handle disconnecting from a friend
def disconnect_option(username, connected_friends):
    username = input("Enter the username of the friend you want to disconnect from: ")
    friend_id = get_username_by_username(username)
    if friend_id in connected_friends:
        disconnect_from_friend(username, friend_id)
        print(f"You are now disconnected from {username}.")
    else:
        print(f"You are not connected with {username}.")

# Define a function to handle accepting friend requests
def accept_request_option(username, pending_requests):
    username = input("Enter the username of the user whose friend request you want to accept: ")
    sender_id = get_username_by_username(username)
    if sender_id in pending_requests:
        accept_friend_request(sender_id, username)
        print(f"You are now friends with {username}.")
    else:
        print(f"No pending friend request from {username}.")

# Define a function to handle rejecting friend requests
def reject_request_option(username, pending_requests):
    username = input("Enter the username of the user whose friend request you want to reject: ")
    sender_id = get_username_by_username(username)
    if sender_id in pending_requests:
        reject_friend_request(sender_id, username)
        print(f"You have rejected the friend request from {username}.")
    else:
        print(f"No pending friend request from {username}.")
