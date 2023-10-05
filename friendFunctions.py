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
