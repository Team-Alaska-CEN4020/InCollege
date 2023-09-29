import textwrap
import time
import globalVars
from generalLinks import aboutUs
from guestControls import *

### External Files ###
from UI import *


def importantLinks():
    exitInput = 0
    while exitInput == 0:
        spacer()
        header('inCollege Important Links')
        print("(1)  Copyright Notice")
        print("(2)  About Us")
        print("(3)  Accessibility")
        print("(4)  User Agreement")
        print("(5)  Privacy Policy")
        print("(6)  Cookie Policy")
        print("(7)  Copyright Policy")
        print("(8)  Brand Policy")
        print("(0)  Languages")

        uInput = input("Input Selection (Q to quit): ")

        if uInput == '1':
            copyrightNotice()
        elif uInput == '2':
            aboutUs() #imported from generalLinks.py
        elif uInput == '3':
            accessibility()
        elif uInput == '4':
            userAgreement()
        elif uInput == '5':
            privacyPolicy()
        elif uInput == '6':
            cookiePolicy()
        elif uInput == '7':
            copyrightPolicy()
        elif uInput == '8':
            brandPolicy()
        elif uInput == '0':
            Languages()
        elif uInput == 'Q' or 'q':
            exitInput = 1
            spacer()
        else:
            print("Invalid Option Try Again")
            spacer()


def copyrightNotice():
    crNoticeText1 = 'Copyright © 2023 TeamAlaska. All rights reserved.'
    crNoticeText2 = 'The content of this website, including text, graphics, images, and other material, is protected under applicable copyright laws and is the property of TeamAlaska. Unauthorized use and/or duplication of this material without express and written permission from TeamAlaska is strictly prohibited.'
    crNoticeText3 = 'For permission requests, write to the owner, addressed “Attention: Permissions Coordinator,” '
    
    wrapText1 = textwrap.fill(crNoticeText1, width=80)
    print("")
    print(wrapText1)
    time.sleep(1)

    wrapText2 = textwrap.fill(crNoticeText2, width=80)
    print("")
    print(wrapText2)
    time.sleep(1)

    wrapText3 = textwrap.fill(crNoticeText3, width=80)
    print("")
    print(wrapText3)
    time.sleep(3)

    return

def accessibility():
    accText = 'At inCollege, we\'re committed to accessibility. We believe in making our applications and services accessible to all users, regardless of ability. Our goal is to provide an inclusive experience by implementing features that support individuals with diverse needs and disabilities. We continuously work to enhance our accessibility and adhere to many of the available standards and guidelines. If you encounter any issues or have suggestions for improvement, please contact us.'
    wrappedText = textwrap.fill(accText, width=80)
    print("")
    print(wrappedText)
    time.sleep(3)
    return

def userAgreement():
    uaText = 'By using the services provided by inCollege, you agree to be bound by the terms and conditions outlined herein. These terms are designed to ensure a safe, secure, and respectful use of our platform for all users. Users must not exploit, misuse, or engage in activities that violate any applicable laws or regulations while using our services. inCollege reserves the right to modify these terms at any time, with changes effective immediately upon posting to our site. Your continued use of our services following any modifications signifies your acceptance of the updated terms. For any queries or concerns regarding this agreement, please contact us.'
    wrappedText = textwrap.fill(uaText, width=80)
    print("")
    print(wrappedText)
    time.sleep(3)
    return

def privacyPolicy():
    ppText = 'inCollege values your privacy. We are committed to safeguarding the privacy of our website visitors and service users. Our policy outlines the type of personal information we collect, how we use it, and the measures we take to secure it. We only collect information necessary for delivering our services and enhancing user experience. Under no circumstances will your data be sold or shared with unauthorized third parties without your consent. Please be aware that our privacy practices may be amended over time as we adapt to new regulatory requirements. For detailed information and updates, kindly contact us.'
    wrappedText = textwrap.fill(ppText, width=80)
    print("")
    print(wrappedText)
    time.sleep(3)
    if globalVars.isLoggedIn == True:
        guestControlSettings()
    else:
        return

def cookiePolicy():
    cpText = 'inCollege uses cookies to enhance your experience while navigating through our website. Cookies are small data files placed on your device that allow us to collect information on how you interact with our services, enabling us to optimize functionality, improve performance, and tailor content to your preferences. By using our site, you consent to the use of cookies in accordance with this policy. For more information on the types and purposes of cookies we use, or to adjust your cookie preferences, please contact us.'
    wrappedText = textwrap.fill(cpText, width=80)
    print("")
    print(wrappedText)
    time.sleep(3)
    return

def copyrightPolicy():
    crpText = 'All content, including text, graphics, logos, images, and software, appearing on inCollege\'s website is the exclusive property of inCollege or its content suppliers and is protected by international copyright laws. Unauthorized use, reproduction, or distribution of this content without the express written consent of inCollege is strictly prohibited. For inquiries about obtaining permission to use any content on our site or for any copyright-related questions, please contact us.'
    wrappedText = textwrap.fill(crpText, width=80)
    print("")
    print(wrappedText)
    time.sleep(3)
    return

def brandPolicy():
    bpText = 'inCollege\'s logos, trademarks, icons, and other intellectual property (“Brand Assets”) are valuable assets that represent our company and products. These Brand Assets should be used in a manner that is consistent with our brand identity, values, and legal guidelines. Unauthorized use, modification, or manipulation of any of inCollege\'s Brand Assets is strictly prohibited. Users and partners wishing to use or refer to inCollege\'s Brand Assets for any public or commercial purpose must obtain written approval from inCollege beforehand. For more information, guidelines, or requests related to our Brand Policy, please contact us.'
    wrappedText = textwrap.fill(bpText, width=80)
    print("")
    print(wrappedText)
    time.sleep(3)
    return

def Languages():
    if globalVars.isLoggedIn == True:
        if globalVars.userSettingLanguage == 0:
            tempLanguage = 'English'
        elif globalVars.userSettingLanguage == 1:
            tempLanguage = 'Spanish'
        else:
            tempLanguage = 'English'
        print("Your current language is set to " + tempLanguage)
        print("Only English and Spanish are supported at this time.")
        uInput = input("Would you like to change your language setting? (Y/N): ")
        if uInput == 'N' or 'n':
            return
        if uInput == 'Y' or 'y':
            if globalVars.userSettingLanguage == 0:
                globalVars.userSettingLanguage == 1
            else:
                globalVars.userSettingLanguage == 0
            cursor.execute("UPDATE users SET language = ? WHERE username = ?",(globalVars.userSettingLanguage, globalVars.username,))
            conn.commit()
            return
    else:
        print("You need to be logged in to do that")
        time.sleep(3)
    return
