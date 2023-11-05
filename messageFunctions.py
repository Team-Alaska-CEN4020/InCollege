# Welcome to the world of message functions
from UI import *
from database import *
import time

def messageInbox(userID):
    loopBreak = True
    cursor.execute("SELECT m.messageID, m.isUnread, u.firstName, m.subject, m.message, m.senderUserID FROM messages m JOIN users u ON m.senderUserID = u.userID WHERE m.recieverUserID = ? ORDER BY m.messageID ASC", (userID,))

    results = cursor.fetchall()

    spacer()
    while loopBreak:
        for idx, row in enumerate(results, start=1):
            is_unread = "Unread" if row[1] == 1 else "Read"
            sender_user_id = row[2]
            subject = row[3]
        
            print(f"{idx}.) {is_unread} - Sender: {sender_user_id}, Subject: {subject}")
            print("\n")
        userInput = input("Type 1 to type a new message or 2 to check your inbox: ")
        if userInput == '1':
            spacer()
            friends = getFriendsList(globalVars.userID)
            sendMessagePrompt(friends)
        elif userInput == '2':
            #check if there are any messages
            if not results:
                print("Your inbox is currently empty.")
                time.sleep(2)
                return

            mInput = int(input("Select a number to the message you would like to read or select 0 to quit: "))
            if mInput == 0:
                loopBreak = False
            else:
                spacer()

                if 1 <= mInput <= len(results):
                    selected_message = results[mInput - 1]
                    unread_status = selected_message[1]
                    if unread_status == 1:
                        cursor.execute("UPDATE messages SET isUnread = 0 WHERE messageID = ?", (selected_message[0],))
                        conn.commit()
                    sender_name = selected_message[2]
                    subject = selected_message[3]
                    message = selected_message[4]
                    recievedFromID= selected_message[5]
                    
                
                    print(f"Sender: {sender_name}\nSubject: {subject}")
                    print(f"Message: {message}")
                else:
                    print("Invalid message number")
                
                mInput = int(input("Type 1 to reply or 0 to return to original menu: "))
                if mInput == 1:
                    replyMessagePrompt(recievedFromID)
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

def sendMessagePrompt (friends):
    reciever = input("Username of who you would like to send it to: ")
    if reciever not in friends and globalVars.userTier == 0: #normal users check
        print("Unable to send a message to that user")
        time.sleep(1)
        print("Try asking them to be friends first!")
        time.sleep(1)
        return
    elif globalVars.userTier == 1: #plus member check
        cursor.execute("SELECT userID FROM users WHERE username =?",(reciever,))
        results = cursor.fetchone()
        if not results:
            print("Sorry, no such user found. Please Try Again")
            time.sleep(2)
            return
        recID = results[0]
    cursor.execute("SELECT userID FROM users WHERE username =?",(reciever,))
    results = cursor.fetchone()
    if not results:
        print("Sorry, no such user found. Please Try Again")
        time.sleep(2)
        return
    recID = results[0]
    subject = input("Enter the subject line of your message: \n")
    message = input("Enter your message (do not use enter): \n")
    
    print("Sending Message Now")
    sendMessage(recID, subject, message)
    time.sleep(3)
    print("Message Sent")

def sendMessage(rec, sub, mes):
    cursor.execute("INSERT INTO messages (senderUserID, recieverUserID, subject, message) VALUES (?,?,?,?)",(globalVars.userID, rec, sub, mes))
    conn.commit()

def replyMessagePrompt(recID):
    print(recID)
    subject = input("Enter the subject line of your message: \n")
    message = input("Enter your message (do not use enter): \n")
    
    print("Sending Message Now")
    sendMessage(recID, subject, message)
    time.sleep(3)
    print("Message Sent")