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
            #counterNum = 0
            userFriendID = []
            for friend in friendsList:
                print(f"Friend ID: {friend[0]}")
                print(f"Name: {friend[1]} {friend[2]}")
                print(f"University: {friend[3]}")
                print(f"Major: {friend[4]}")
                userFriendID.append(friend[0])
                #print(f"Press {counterNum+1} to View Profile:")
                print("\n")
                #counterNum = counterNum+1
            while True: 
                spacer()
                print("Please select from the following menu options: ")
                print("1. View a friend's profile")
                print("2. Disconnect from a friend")
                print ("3. Return to previous menu ")
                choice = input("Please enter (1/2/3): ")

                if choice == '1':
                    #print("Please enter the Friend ID number to View Profile:")
                    uInput = int(input("Please enter the Friend ID number to View Profile:"))
                    for id in userFriendID:
                        if uInput == id:
                            showFriendProfile(id)
                    #spacer()
                    continue

                elif choice == '2': 
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
                    continue
                elif choice == '3' :
                    spacer()
                    return 
                    

        else:
            print("No one is in your network at the moment.")
        
    except Exception as e:
        print(f"Error occurred while fetching friends: {e}")



###########################################Epic-5 FUNCTIONS###############################################


def showFriendProfile(friendID):
    spacer()
    header('Friend Profile')

    try: 

        # Query the database to retrieve and display the friend's profile details based on their User ID        
        #cursor.execute("SELECT * FROM users WHERE userID = ? AND marketingEmail = 1", (friendID,))
        cursor.execute("SELECT * FROM profiles WHERE userID = ?", (friendID,))
        friend_data = cursor.fetchone()

        cursor.execute("SELECT * FROM users WHERE userID = ?", (friendID,))
        user_name = cursor.fetchone()

        header(
            f"{user_name[3]} {user_name[4]}'s Profile:\n")

        if friend_data:
            print(f"Title: {friend_data[2]}")
            print(f"Major: {friend_data[3]}")
            print(f"University: {friend_data[4]}")
            print(f"About: {friend_data[5]}")

            # Fetch experience and education from their respective tables based on the user's ID
            #cursor.execute("SELECT * FROM experience WHERE userID = ?", (globalVars.userID,))
            cursor.execute("""
                SELECT e.experienceID, e.userID, e.jobTitle, e.employer, e.dateStarted, e.dateEnded, e.location, e.description
                FROM experience as e
                JOIN users as u ON e.userID = u.userID 
                WHERE e.userID = ?""", (friendID,))
            experience_data = cursor.fetchall()

            if experience_data:
                print("Experience:")
                for exp in experience_data:
                    print("  - Job Title:", exp[2])
                    print("    Employer:", exp[3])
                    print("    Date Started:", exp[4])
                    print("    Date Ended:", exp[5])
                    print("    Location:", exp[6])
                    print("    Description:", exp[7])

            cursor.execute("""
                SELECT edu.userID, edu.schoolName, edu.degree, edu.yearsAttended, u.userID
                FROM education as edu
                JOIN users as u ON edu.userID = u.userID 
                WHERE edu.userID = ?""", (friendID,))
            education_data = cursor.fetchall()

            if education_data:
                print("\nEducation:")
                for edu in education_data:
                    print("  - School Name:", edu[1])
                    print("    Degree:", edu[2])
                    print("    Years Attended:", edu[3])
        else:
            print("\nFriend not found in the database.")

    except Exception as e:
        print(f"Error occurred while fetching friends profiles: {e}")
    #input("Press Enter to Continue...")
