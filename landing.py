### Libraries ###
import time

### External Files ###
from UserCreateLogin import *
from userStories import *
from testimonial import *
from usefulLinks import *
from UI import *
from important import *
from userSearch import *


def startupLanding():
    # Call up a story to display
    testimonialStory()
    
    # User menu loop
    exitInput = 0
    while exitInput == 0:
        spacer()
        header('Welcome to inCollege')
        print("(1)  Login")
        print("(2)  Sign up")
        print("(3)  Look up a user")
        print("(4)  Watch Video")
        print("(5)  Useful Links")
        print("(0)  inCollege Important Links")

        uInput = input("Input Selection (Q to quit): ")

        # Once an option is picked we then will choose which function that needs to be done
        if uInput == '1':
            UserLogin()
        elif uInput == '2':
            createUser()
        elif uInput == '3':
            userSearch()
        elif uInput == '4':
            videoPlay()
        elif uInput == '5':
            usefulLinksMenu()
        elif uInput == '0':
            importantLinks()
        elif uInput.upper() == 'Q':
            exitInput = 1
        else:
            print("Invalid Option. Try Again")
            time.sleep(3)
