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



# def getFriends():
#     spacer()
#     header('Your Network')

#     try:
#         cursor.execute("""
#             SELECT f.friendUserID, u.firstName, u.lastName, u.userUniversity, u.userMajor
#             FROM friends AS f
#             JOIN users AS u ON f.friendUserID = u.userID
#             WHERE f.userID = ? AND f.friendshipStatus = 1 AND f.isDeleted = 0
#         """, (globalVars.userID,))
#         friendsList = cursor.fetchall()

#         if friendsList:
#             for friend in friendsList:
#                 print(f"Friend ID: {friend[0]}")
#                 print(f"Name: {friend[1]} {friend[2]}")
#                 print(f"University: {friend[3]}")
#                 print(f"Major: {friend[4]}")
#                 print("\n")
#             # Prompt user to disconnect from a friend
#             while True:
#                 userResponse = input("Enter the ID of a friend you want to disconnect from (or 'Q' to quit): ")
#                 if userResponse.upper() == 'Q':
#                     break
#                 try:
#                     selectedFriendID = int(userResponse)
#                     updateFriendDisconnect(selectedFriendID)
#                 except ValueError:
#                     print("Invalid input. Please enter a valid Friend ID or 'Q' to quit.")

#         else:
#             print("No one is in your network at the moment.")
#     except Exception as e:
#         print(f"Error occurred while fetching friends: {e}")

#     input("Press Enter to Continue...")

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
                print("Press 1 to View Profile:")
                print("\n")

                uInput = input("Input Selection (Q to quit and return): ")
                if uInput == '1':
                    interactWithFriend()

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

    #input("Press Enter to Continue...")

###########################################Epic-5 FUNCTIONS###############################################

def interactWithFriend(friendID):
    spacer()
    header('Friend Profile')

    # Query the database to retrieve and display the friend's profile details based on their User ID        
    cursor.execute("SELECT * FROM users WHERE userID = ? AND marketingEmail = 1", (friendID,))
    friend_data = cursor.fetchone()

    if friend_data:
        print(f"User ID: {friend_data[0]}")
        print(f"Username: {friend_data[1]}")
        print(f"Name: {friend_data[2]} {friend_data[3]}")
        print(f"University: {friend_data[4].upper()}")
        print(f"Major: {friend_data[5].capitalize()}")
        # Add more profile details here as needed
    else:
        print("\nFriend not found in the database.")

    input("Press Enter to Continue...")




def viewFriendProfiles():
    spacer()
    header('View Friend Profiles')

    # Query to get a list of your friends
    cursor.execute("""
        SELECT u.userID, u.username, u.firstName, u.lastName
        FROM friends AS f
        JOIN users AS u ON f.friendUserID = u.userID
        WHERE f.userID = ? AND f.friendshipStatus = 1 AND f.isDeleted = 0
    """, (globalVars.userID,))
    friends = cursor.fetchall()

    if not friends:
        print("\nYou don't have any friends to view profiles.")
        input("Press Enter to Continue...")
        return

    # Display your list of friends
    print("Your Friends:")
    for i, friend in enumerate(friends, start=1):
        print(f"{i}. User ID: {friend[0]}, Username: {friend[1]}, Name: {friend[2]} {friend[3]}")

    # Ask the user to select a friend to view their profile
    while True:
        userResponse = input("\nEnter the number of the friend whose profile you want to view (or 'Q' to quit): ")
        if userResponse.upper() == 'Q':
            break
        try:
            selected_index = int(userResponse)
            if 1 <= selected_index <= len(friends):
                selected_friend = friends[selected_index - 1]
                viewUserProfile(selected_friend[0])  # Call a function to view the selected friend's profile
            else:
                print("Invalid input. Please enter a valid number or 'Q' to quit.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'Q' to quit.")

    input("Press Enter to Continue...")

def viewUserProfile(userID):
    # Query the database to retrieve and display the user's profile details based on their User ID
    cursor.execute("SELECT * FROM users WHERE userID = ?", (userID,))
    user_data = cursor.fetchone()

    if user_data:
        print("\nUser Profile:")
        print(f"User ID: {user_data[0]}")
        print(f"Username: {user_data[1]}")
        print(f"Name: {user_data[2]} {user_data[3]}")
        print(f"University: {user_data[4].upper()}")
        print(f"Major: {user_data[5].capitalize()}")
        # Add more profile details here as needed
    else:
        print("\nUser not found in the database.")

    input("Press Enter to Continue...")
