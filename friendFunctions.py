from database import *

# Define a function to get user information by user_id
def get_user_info(user_id):
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user_info = cursor.fetchone()
    if user_info:
        return {
            'id': user_info[0],
            'username': user_info[1],
            'firstName': user_info[2],
            'lastName': user_info[3],
            'major': user_info[4],
            'university': user_info[5],
        }
    return None

# Define a function to get user_id by username
def get_user_id_by_username(username):
    cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
    user_id = cursor.fetchone()
    if user_id:
        return user_id[0]
    return None

# Define a function to handle disconnecting from a friend
def disconnect_option(user_id, connected_friends):
    username = input("Enter the username of the friend you want to disconnect from: ")
    friend_id = get_user_id_by_username(username)
    if friend_id in connected_friends:
        disconnect_from_friend(user_id, friend_id)
        print(f"You are now disconnected from {username}.")
    else:
        print(f"You are not connected with {username}.")

# Define a function to handle accepting friend requests
def accept_request_option(user_id, pending_requests):
    username = input("Enter the username of the user whose friend request you want to accept: ")
    sender_id = get_user_id_by_username(username)
    if sender_id in pending_requests:
        accept_friend_request(sender_id, user_id)
        print(f"You are now friends with {username}.")
    else:
        print(f"No pending friend request from {username}.")

# Define a function to handle rejecting friend requests
def reject_request_option(user_id, pending_requests):
    username = input("Enter the username of the user whose friend request you want to reject: ")
    sender_id = get_user_id_by_username(username)
    if sender_id in pending_requests:
        reject_friend_request(sender_id, user_id)
        print(f"You have rejected the friend request from {username}.")
    else:
        print(f"No pending friend request from {username}.")
