import sqlite3
# SQLite database setup
# Connect to the SQLite database (creates 'user_data.db' if it doesn't exist)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()  # Create a cursor object to execute SQL commands

def insertFriendRequests(fromID, toID):
    #note: for reqStatus, 0 = requested, 1 = accepted, 2 = rejected. Rejected requests should also have isDeleted flagged as 1
    cursor.execute("INSERT INTO friendRequests (fromUserID, toUserID, reqStatus) VALUES (?,?,?)",(fromID, toID, 0))
    conn.commit()