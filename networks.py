#networks.py>
import time
from database import *
import sqlite3


def showMyNetwork(user_id):
    connected_friends = get_user_friends(user_id)
    
    if not connected_friends:
        print("You don't have any connected friends.")
    else:
        print("Your connected friends:")
        for friend_id in connected_friends:
            friend_info = get_user_info(friend_id)
            print(f"- Name: {friend_info['firstName']} {friend_info['lastName']}")
            print(f"  Username: {friend_info['username']}")
            print(f"  Major: {friend_info['major']}")
            print(f"  University: {friend_info['university']}")
            print(f"  Status: Connected")
            print("  (D) Disconnect from this friend")

        choice = input("Enter the option (Q to quit): ")
        if choice == 'Q' or choice == 'q':
            return
        elif choice == 'D' or choice == 'd':
            disconnect_option(user_id, connected_friends)
        else:
            print("Invalid Option. Try Again.")



def sendFriendRequest(user_id):
    username = input("Enter the username of the person you want to send a friend request to: ")
    friend_id = get_user_id_by_username(username)
    
    if friend_id is not None:
        # Check if the user is already friends with the person
        if friend_id in get_user_friends(user_id):
            print(f"You are already friends with {username}.")
        else:
            # Check if a friend request has already been sent
            if friend_id in get_pending_friend_requests(user_id):
                print("A friend request has already been sent to this user.")
            else:
                send_friend_request(user_id, friend_id)
                print(f"Friend request sent to {username}.")
    else:
        print(f"No user found with the username {username}.")

# ...

def viewFriendRequests(user_id):
    pending_requests = get_pending_friend_requests(user_id)
    
    if not pending_requests:
        print("You don't have any pending friend requests.")
    else:
        print("Your pending friend requests:")
        for sender_id in pending_requests:
            sender_info = get_user_info(sender_id)
            print(f"- Name: {sender_info['firstName']} {sender_info['lastName']}")
            print(f"  Username: {sender_info['username']}")
            print("  (A) Accept Request")
            print("  (R) Reject Request")
        
        choice = input("Enter the option (Q to quit): ")
        if choice == 'Q' or choice == 'q':
            return
        elif choice == 'A' or choice == 'a':
            accept_request_option(user_id, pending_requests)
        elif choice == 'R' or choice == 'r':
            reject_request_option(user_id, pending_requests)
        else:
            print("Invalid Option. Try Again.")
