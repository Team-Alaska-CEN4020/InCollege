import sqlite3
import globalVars
# SQLite database setup
# Connect to the SQLite database (creates 'user_data.db' if it doesn't exist)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()  # Create a cursor object to execute SQL commands

def insertFriendRequest(fromID, toID):
    #note: for reqStatus, 0 = requested, 1 = accepted, 2 = rejected. Rejected requests should also have isDeleted flagged as 1
    cursor.execute("INSERT INTO friendRequests (fromUserID, toUserID, reqStatus) VALUES (?,?,?)",(fromID, toID, 0))
    conn.commit()

def updateFriendRequest(userID, status):
    # Update the friendRequest table
    cursor.execute("SELECT * FROM friendRequests WHERE fromUserID = ? AND toUserID = ? AND isDeleted = 0 AND reqStatus = 0", (userID, globalVars.userID,))
    if not cursor.fetchone():
        print("Invalid user ID or no pending request from this user.")
        return

    cursor.execute("UPDATE friendRequests SET reqStatus = ? WHERE fromUserID = ? AND toUserID = ?", (status, userID, globalVars.userID,))
    conn.commit()

    if status == 1:
        insertFriend(userID)
    elif status == 2:
        print(f"Friend request from userID {userID} rejected!")

def insertFriend(friendID):
    try:
        cursor.execute("INSERT INTO friends (userID, friendUserID, friendshipStatus, isDeleted) VALUES (?, ?, 1, 0)", (globalVars.userID, friendID,))
        conn.commit()
        cursor.execute("INSERT INTO friends (userID, friendUserID, friendshipStatus, isDeleted) VALUES (?, ?, 1, 0)", (friendID, globalVars.userID,))
        conn.commit()
        print(f"Friend request from userID {friendID} accepted!")
    except Exception as e:
        print(f"Error occurred while adding friend: {e}")

def updateFriendDisconnect(friendID):
    try:
        # Set friendshipStatus to 0 for both user and friend
        cursor.execute("UPDATE friends SET friendshipStatus = 0 WHERE userID = ? AND friendUserID = ? AND isDeleted = 0", (globalVars.userID, friendID,))
        conn.commit()
        cursor.execute("UPDATE friends SET friendshipStatus = 0 WHERE userID = ? AND friendUserID = ? AND isDeleted = 0", (friendID, globalVars.userID,))
        conn.commit()
        print(f"You have disconnected from friend with ID: {friendID}")
    except Exception as e:
        print(f"Error occurred while disconnecting friend: {e}")

def getFriendsList(userID):
    import time
    print("Friends List: ")
    try:
        cursor.execute("SELECT u.username FROM users AS u JOIN friends AS f ON u.userID = f.friendUserID WHERE f.userID = ? and f.friendshipStatus = 1 and f.isDeleted = 0",(userID,))
        friends = cursor.fetchall()    
    except Exception as e:
        print(f"Error occurred while finding friends: {e}")
    if not friends:
        print("It looks like you havn't made any friends yet.")
        time.sleep(2)
        return
    else:
        for friend in friends:
            print(f"- {friend[0]}")
    friendsList = [friend[0] for friend in friends] or []
    return friendsList