# Welcome to the world of message functions
from UI import *
from database import *
import time

def messageInbox(userID):
    loopBreak = True
    cursor.execute("SELECT m.isUnread, u.firstName, m.subject, m.message FROM messages m JOIN users u ON m.senderUserID = u.userID WHERE m.recieverUserID = ? ORDER BY m.messageID ASC", (userID,))

    results = cursor.fetchall()

    spacer()
    while loopBreak:
        for idx, row in enumerate(results, start=1):
            is_unread = "Unread" if row[0] == 1 else "Read"
            sender_user_id = row[1]
            subject = row[2]
        
            print(f"{idx}.) {is_unread} - Sender: {sender_user_id}, Subject: {subject}")
            print("\n")
        userInput = input("Type 1 to type a new message or 2 to continue: ")
        if userInput == '1':
            spacer()
            print("Creating a message Under construction")
        elif userInput == '2':
            mInput = int(input("Select a number to the message you would like to read or select 0 to quit: "))
            if mInput == 0:
                loopBreak = False
            else:
                spacer()

                if 1 <= mInput <= len(results):
                    selected_message = results[mInput - 1]
                    sender_name = selected_message[1]
                    subject = selected_message[2]
                    message = selected_message[3]
                
                    print(f"Sender: {sender_name}\nSubject: {subject}")
                    print(f"Message: {message}")
                else:
                    print("Invalid message number")
                
                mInput = int(input("Type 1 to reply or 0 to return to original menu: "))
                if mInput == 1:
                    print("Reply function is under construction")
                elif mInput == 0:
                    loopBreak = False

def checkUnreadStatusLogin(userID):
    cursor.execute("SELECT COUNT(*) as unreadMessages FROM messages WHERE isUnread = 1 AND recieverUserID = ?", (userID,))
    result = cursor.fetchone()
    if result[0] >= 1:
        print("***Please check your inbox! You have an unread message.***")
        time.sleep(2)
    else:
        return
    
def checkUnreadStatus(userID):
    cursor.execute("SELECT COUNT(*) as unreadMessages FROM messages WHERE isUnread = 1 AND recieverUserID = ?", (userID,))
    result = cursor.fetchone()
    if result[0] >= 1:
        print("(2) Unread Messages")
    else:
        return

def updateIfUnread(userID):
    