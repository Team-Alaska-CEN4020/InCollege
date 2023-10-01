### Libraries ###
#import os

### External Files ###
from UserCreateLogin import *
from userStories import *
from testimonial import *
from usefulLinks import *
from UI import *
from important import *
import globalVars

def clear_screen():
  """ not working at the moment refactor for later story
  if os.name == 'posix':  # For Unix/Linux/MacOS
        os.system('clear')
  elif os.name == 'nt':  # For Windows
        os.system('cls')
  """
  
def startupLanding():
    clear_screen()
    
  
    #User stories
    cursor.execute("SELECT story FROM stories")
    userStory = cursor.fetchall()
  
    print("User Stories: ")
    print(userStory[random_number])
    print("\n")
  
    # User menu
    print("Welcome to inCollege: inCollege is your")
    print("Login: (1)")
    print("Sign up: (2) ")
    print("Delete Users: (3)")
    print("Look up a user: (4)")
    print("Watch Video: (5)")
=======
    # Call up a story to display
    testimonialStory()
    
    # User menu loop
    exitInput = 0
    while exitInput == 0:
        header('Welcome to inCollege')
        print("(1)  Login")
        print("(2)  Sign up")
        print("(3)  Delete Users")
        print("(4)  Look up a user")
        print("(5)  Watch Video")
        print("(6)  Useful Links")
        print("(0)  inCollege Important Links")

        uInput = input("Input Selection (Q to quit): ")
>>>>>>> Epic3-menus

        # Once option is picked we then will choose which function that needs to be done
        if uInput == '1':
            UserLogin()
        elif uInput == '2':
            createUser()
        elif uInput == '3':
            deleteUser()
        elif uInput == '4':
            searchUser()
        elif uInput == '5':
            videoPlay()
        elif uInput == '6':
            usefulLinksMenu()
        elif uInput == '0':
            importantLinks()
        elif uInput == 'Q' or 'q':
            exitInput = 1
            spacer()
        else:
            print("Invalid Option Try Again")
            spacer()
