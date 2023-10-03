import sqlite3
# SQLite database setup
# Connect to the SQLite database (creates 'user_data.db' if it doesn't exist)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()  # Create a cursor object to execute SQL commands

# Create a table to store user data if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        firstName TEXT,
        lastName TEXT, 
        major TEXT,
        university TEXT
    )
''')
#######University and major column not forming, need to work on that##########


# Create a table to store user stories if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS stories (
        story TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        title TEXT,
        description TEXT,
        employer TEXT,
        location TEXT,
        salary TEXT,
        firstname TEXT,
        lastname TEXT
    )
''')

# conn.commit()
# MAX_ACCOUNTS = 10
# MAX_JOBS = 5



##################################EPIC 4 ############################################
# #Creating Friends table 
from friendFunctions import get_user_info, disconnect_option, get_username_by_username, accept_request_option, reject_request_option



# # Create a table to store friend connections if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS friends (
        username TEXT,
        friend_id INTEGER,
        status TEXT,
        FOREIGN KEY (username) REFERENCES users(id),
        FOREIGN KEY (friend_id) REFERENCES users(id)
    )
''')

# # Create a table to store pending friend requests if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS friend_requests (
        sender_id INTEGER,
        receiver_id INTEGER,
        status TEXT,
        FOREIGN KEY (sender_id) REFERENCES users(id),
        FOREIGN KEY (receiver_id) REFERENCES users(id)
    )
''')

# # Add a 'friends' column to the 'users' table to store the count of friends
# cursor.execute('''
#     ALTER TABLE users
#     ADD COLUMN friends INTEGER DEFAULT 0
# ''')

conn.commit()

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
MAX_ACCOUNTS = 10
MAX_JOBS = 5
