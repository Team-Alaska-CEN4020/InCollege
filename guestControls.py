import globalVars
from UI import *
from database import *

def guestControlSettings():
    
    exitInput = 0
    while exitInput == 0:
        spacer()
        header('Guest Controls: ')
        uInput = input("Would you like to view/change your user settings? (Y/N): ")

        if uInput.lower() == 'n':  # Simplified the input checking
            exitInput = 1
        elif uInput.lower() == 'y':
            exitSubInput = 0
            while exitSubInput == 0:
                spacer()
                
                # The function is now being used to both print and get the status dynamically
                tempEmail, tempSMS, tempAdTarget, tempLanguage = getAndDisplaySettings()

                uinput = input("Which setting would you like to toggle (Q to quit and return): ")

                # Input handling here...
                # After changing a setting, the getAndDisplaySettings() function will be called again due to the loop.
                
                if uinput == '1':
                    globalVars.userSettingMarketingEmail = not globalVars.userSettingMarketingEmail
                elif uinput == '2':
                    globalVars.userSettingMarketingSMS = not globalVars.userSettingMarketingSMS
                elif uinput == '3':
                    globalVars.userSettingAdvertisementTargeted = not globalVars.userSettingAdvertisementTargeted
                elif uinput == '4':
                    globalVars.userSettingLanguage ^= 1
                elif uinput.lower() == 'q':
                    # Update database with new changes
                    cursor.execute("UPDATE users SET marketingEmail = ?, marketingSMS = ?, adsTargeted = ?, language = ? WHERE username = ?",(globalVars.userSettingMarketingEmail, globalVars.userSettingMarketingSMS, globalVars.userSettingAdvertisementTargeted, globalVars.userSettingLanguage, globalVars.username,))
                    conn.commit()
                    
                    exitSubInput = 1
                else:
                    print("Invalid Option Try Again")
                
def getAndDisplaySettings():
    """Function to get and display the current settings"""
    print("Here are your current settings.")
    
    tempEmail = 'Enabled' if globalVars.userSettingMarketingEmail else 'Disabled'
    tempSMS = 'Enabled' if globalVars.userSettingMarketingSMS else 'Disabled'
    tempAdTarget = 'Enabled' if globalVars.userSettingAdvertisementTargeted else 'Disabled'
    tempLanguage = 'English' if globalVars.userSettingLanguage == 0 else 'Spanish'
    
    print("(1)  Receiving inCollege Emails -        " + tempEmail)
    print("(2)  Receiving inCollege Texts -         " + tempSMS)
    print("(3)  Receiving Targeted Advertisement -  " + tempAdTarget)
    print("(4)  Current Language Setting -          " + tempLanguage)
    
    return tempEmail, tempSMS, tempAdTarget, tempLanguage