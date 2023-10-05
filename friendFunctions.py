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
    if sentRequests:
        print("\nFriend Requests Sent:")
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
    print("\n")
    header("Friend Requests Received")
    if receivedRequests:
        for req in receivedRequests:
            print("ID:        \t", req[1])
            print("First Name:\t", req[2])
            print("Last Name: \t", req[3])
            print("University:\t", req[4].upper())
            print("Major:     \t", req[3].capitalize())
            print("\n")
    else:
        print("\nYou have not received any friend requests.")

    input("Press Enter to Continue...")
    

# fix later
# def showMyNetwork(user_id):
#     connected_friends = get_user_friends(user_id)
    
#     if not connected_friends:
#         print("You don't have any connected friends.")
#     else:
#         print("Your connected friends:")
#         for friend_id in connected_friends:
#             friend_info = get_user_info(friend_id)
#             print(f"- Name: {friend_info['firstName']} {friend_info['lastName']}")
#             print(f"  Username: {friend_info['username']}")
#             print(f"  Major: {friend_info['major']}")
#             print(f"  University: {friend_info['university']}")
#             print(f"  Status: Connected")
#             print("  (D) Disconnect from this friend")

#         choice = input("Enter the option (Q to quit): ")
#         if choice == 'Q' or choice == 'q':
#             return
#         elif choice == 'D' or choice == 'd':
#             disconnect_option(user_id, connected_friends)
#         else:
#             print("Invalid Option. Try Again.")
#             
