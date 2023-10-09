from database import *
from UserCreateLogin import *
import globalVars
from UI import *

def viewFriendRequests():
    spacer()
    header('Pending Friend Requests')

    # Query to get all friend requests sent by the current user
    cursor.execute("""
        SELECT fr.friendReqID, fr.toUserID, u.firstName, u.lastName
        FROM friendRequests as fr
        JOIN users as u ON fr.toUserID = u.userID
        WHERE fr.fromUserID = ? AND fr.isDeleted = 0 AND fr.reqStatus = 0
        """, (globalVars.userID,))
    sentRequests = cursor.fetchall()

    # Print all friend requests sent by the current user
    print("\nFriend Requests Sent:")
    if sentRequests:    
        for req in sentRequests:
            print(f"To User ID: {req[1]}, Name: {req[2]} {req[3]}")
    else:
        print("\nYou have not sent any friend requests.")

    # Query to get all friend requests received by the current user
    cursor.execute("""
        SELECT fr.friendReqID, fr.fromUserID, u.firstName, u.lastName, u.userUniversity, u.userMajor
        FROM friendRequests as fr
        JOIN users as u ON fr.fromUserID = u.userID
        WHERE fr.toUserID = ? AND fr.isDeleted = 0 AND fr.reqStatus = 0
        """, (globalVars.userID,))
    receivedRequests = cursor.fetchall()

    # Print all friend requests received by the current user
    print("\nFriend Requests Received:")
    if receivedRequests:
        for req in receivedRequests:
            print("ID:        \t", req[1])
            print("Name:      \t", req[2], " ", req[3])
            print("University:\t", req[4].upper())
            print("Major:     \t", req[3].capitalize())
            print("\n")
        
        # Asks user if they want to accept any requests
        while True:
            userResponse = input("Enter the ID of a user whose friend request you want to ACCEPT (or 'Q' to quit): ")
            if userResponse.upper() == 'Q':
                break
            try:
                selectedUserID = int(userResponse)
                updateFriendRequest(selectedUserID,1)  
            except ValueError:
                print("Invalid input. Please enter a valid user ID or 'Q' to quit.")
        
        # Asks user if they want to reject any requests
        while True:
            userResponse = input("Enter the ID of a user whose friend request you want to REJECT (or 'Q' to to quit): ")
            if userResponse.upper() == 'Q':
                break
            try:
                selectedUserID = int(userResponse)
                updateFriendRequest(selectedUserID,2)  
            except ValueError:
                print("Invalid input. Please enter a valid user ID or 'Q' to finish rejecting.")
    
    else:
        print("\nYou have not received any friend requests.")

    input("Press Enter to Continue...")

def getFriends():
    spacer()
    header('Your Network')

    try:
        cursor.execute("""
            SELECT f.friendUserID, u.firstName, u.lastName, u.userUniversity, u.userMajor
            FROM friends AS f
            JOIN users AS u ON f.friendUserID = u.userID
            WHERE f.userID = ? AND f.friendshipStatus = 1 AND f.isDeleted = 0
        """, (globalVars.userID,))
        friendsList = cursor.fetchall()

        if friendsList:
            for friend in friendsList:
                print(f"Friend ID: {friend[0]}")
                print(f"Name: {friend[1]} {friend[2]}")
                print(f"University: {friend[3]}")
                print(f"Major: {friend[4]}")
                print("\n")
            # Prompt user to disconnect from a friend
            while True:
                userResponse = input("Enter the ID of a friend you want to disconnect from (or 'Q' to quit): ")
                if userResponse.upper() == 'Q':
                    break
                try:
                    selectedFriendID = int(userResponse)
                    updateFriendDisconnect(selectedFriendID)
                except ValueError:
                    print("Invalid input. Please enter a valid Friend ID or 'Q' to quit.")

        else:
            print("No one is in your network at the moment.")
    except Exception as e:
        print(f"Error occurred while fetching friends: {e}")

    input("Press Enter to Continue...")