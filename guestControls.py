import globalVars
from UI import *
from database import *

def guestControlSettings():
    
    exitInput = 0
    while exitInput == 0:
        spacer()
        header('Guest Controls')
        uInput = input("Would you like to view/change your user settings? (Y/N): ")

        if uInput == 'N' or 'n':
            exitInput = 1
        elif uInput == 'Y' or 'y':
            exitSubInput = 0
            while exitSubInput == 0:
                spacer()
                print("Here are your current settings.")
            
                if globalVars.userSettingMarketingEmail == True:
                    tempEmail = 'Enabled'
                else:
                    tempEmail = 'Disabled'

                if globalVars.userSettingMarketingSMS == True:
                    tempSMS = 'Enabled'
                else:
                    tempSMS = 'Disabled'
            
                if globalVars.userSettingAdvertisementTargeted == True:
                    tempAdTarget = 'Enabled'
                else:
                    tempAdTarget = 'Disabled'
            
                if globalVars.userSettingLanguage == 0:
                    tempLanguage = 'English'
                elif globalVars.userSettingLanguage == 1:
                    tempLanguage = 'Spanish'
                else:
                    tempLanguage = 'English'

                print("(1)  Recieving inCollege Emails -        " + tempEmail)
                print("(2)  Recieving inCollege Texts -         " + tempSMS)
                print("(3)  Recieving Targeted Advertisement -  " + tempAdTarget)
                print("(4)  Current Language Setting -          " + tempLanguage)
                
                uinput = input("Which setting would you like to toggle (Q to quit and return): ")

                if uInput == '1':
                    if globalVars.userSettingMarketingEmail == True:
                        globalVars.userSettingMarketingEmail == False
                    else:
                        globalVars.userSettingMarketingEmail == True
                elif uInput == '2':
                    if globalVars.userSettingMarketingSMS == True:
                        globalVars.userSettingMarketingSMS == False
                    else:
                        globalVars.userSettingMarketingSMS == True
                elif uInput == '3':
                    if globalVars.userSettingAdvertisementTargeted == True:
                        globalVars.userSettingAdvertisementTargeted == False
                    else:
                        globalVars.userSettingAdvertisementTargeted == True
                elif uInput == '4':
                    if globalVars.userSettingLanguage == 0:
                        globalVars.userSettingLanguage == 1
                    else:
                        globalVars.userSettingLanguage == 0
                elif uInput == 'Q' or 'q':
                    # Update database with new changes
                    # Need to figure out how to make this more readable later
                    cursor.execute("UPDATE users SET marketingEmail = ?, marketingSMS = ?, adsTargeted = ?, language = ? WHERE username = ?",(globalVars.userSettingMarketingEmail, globalVars.userSettingMarketingSMS, globalVars.userSettingAdvertisementTargeted, globalVars.userSettingLanguage, globalVars.username,))
                    conn.commit()
                    
                    exitSubInput = 1
                else:
                    print("Invalid Option Try Again")
            
            return