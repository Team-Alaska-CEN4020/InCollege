# Welcome to the world of message functions
from UI import *
from database import *
import time

def messageInbox(userID):
    loopBreak = True
    cursor.execute("SELECT m.messageID, m.isUnread, u.firstName, m.subject, m.message FROM messages m JOIN users u ON m.senderUserID = u.userID WHERE m.recieverUserID = ? ORDER BY m.messageID ASC", (userID,))

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
            print("Creating a message Under construction")
            getFriendsList(globalVars.userID)
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

def sendMessagePrompt ():
    print("take in stuff")

def sendMessage():
    print("do stuff with inputs")