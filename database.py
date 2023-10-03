import sqlite3
# SQLite database setup
# Connect to the SQLite database (creates 'user_data.db' if it doesn't exist)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()  # Create a cursor object to execute SQL commands


##################################EPIC 4 ############################################
# #Creating Friends table 
from friendFunctions import *

# # Define a function to send a friend request
def send_friend_request(sender_id, receiver_id):
    cursor.execute('INSERT INTO friend_requests (sender_id, receiver_id, status) VALUES (?, ?, "pending")', (sender_id, receiver_id))
    conn.commit()

# Define a function to accept a friend request
def accept_friend_request(sender_id, receiver_id):
    cursor.execute('UPDATE friend_requests SET status = "accepted" WHERE sender_id = ? AND receiver_id = ?', (sender_id, receiver_id))
    cursor.execute('INSERT INTO friends (username, friend_id, status) VALUES (?, ?, "connected")', (sender_id, receiver_id))
    cursor.execute('INSERT INTO friends (username, friend_id, status) VALUES (?, ?, "connected")', (receiver_id, sender_id))
    cursor.execute('UPDATE users SET friends = friends + 1 WHERE id = ?', (sender_id,))
    cursor.execute('UPDATE users SET friends = friends + 1 WHERE id = ?', (receiver_id,))
    conn.commit()

# Define a function to reject a friend request
def reject_friend_request(sender_id, receiver_id):
    cursor.execute('UPDATE friend_requests SET status = "rejected" WHERE sender_id = ? AND receiver_id = ?', (sender_id, receiver_id))
    conn.commit()

# Define a function to disconnect from a friend
def disconnect_from_friend(username, friend_id):
    cursor.execute('DELETE FROM friends WHERE (username = ? AND friend_id = ?) OR (username = ? AND friend_id = ?)', (username, friend_id, friend_id, username))
    cursor.execute('UPDATE users SET friends = friends - 1 WHERE id = ? OR id = ?', (username, friend_id))
    conn.commit()

# Define a function to get a user's pending friend requests
def get_pending_friend_requests(username):
    cursor.execute('SELECT sender_id FROM friend_requests WHERE receiver_id = ? AND status = "pending"', (username,))
    requests = cursor.fetchall()
    return [request[0] for request in requests]

# Define a function to get a user's friends
def get_user_friends(username):
    cursor.execute('SELECT username, friend_id FROM friends WHERE (username = ? OR friend_id = ?) AND status = "connected"', (username, username))
    friend_records = cursor.fetchall()
    friends = []
    for record in friend_records:
        if record[0] == username:
            friends.append(record[1])
        else:
            friends.append(record[0])
    return friends
# SQL command to create a 'users' table with 'username' and 'password' columns if it doesn't exist
conn.commit()

