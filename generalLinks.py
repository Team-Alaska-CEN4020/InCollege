### External Files ###
from UI import *
from UserCreateLogin import *
import globalVars
import textwrap
import time

def generalLinksMenu():
    exitInput = 0
    while exitInput == 0:
        spacer()
        header('General Links')
        print("(1)  Sign Up")
        print("(2)  Help Center")
        print("(3)  About")
        print("(4)  Press")
        print("(5)  Blog")
        print("(6)  Careers")
        print("(7)  Developers")

        uInput = input("Input Selection (Q to quit and return): ")

        if uInput == '1':
            if globalVars.isLoggedIn == True:
                print("User Is Already Logged In")
            else:
                createUser()
        elif uInput == '2':
            helpCenter()
        elif uInput == '3':
            aboutUs()
        elif uInput == '4':
            press()
        elif uInput == '5':
            blog()
        elif uInput == '6':
            careers()
        elif uInput == '7':
            developersInfo()
        elif uInput == 'Q' or 'q':
            exitInput = 1
        else:
            print("Invalid Option Try Again")


def helpCenter():
    print("We're here to help")
    time.sleep(3)
    return

def aboutUs():
    aboutUsText = 'inCollege: Welcome to inCollege, the world\'s largest college student network with many users in many countries and territories worldwide.'
    wrappedText = textwrap.fill(aboutUsText, width=80)
    print("")
    print(wrappedText)
    time.sleep(3)
    return

def press():
    pressText = 'inCollege Pressroom: Stay on top of the latest news, updates, and reports'
    wrappedText = textwrap.fill(pressText, width=80)
    print("")
    print(wrappedText)
    time.sleep(3)
    return

def blog():
    print("")
    print("Under construction")
    time.sleep(2)
    return

def careers():
    print("")
    print("Under construction")
    time.sleep(2)
    return

def developersInfo():
    print("")
    print("Under construction")
    time.sleep(2)
    return