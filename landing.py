from UserCreateLogin import *
from userStories import *
from testimonial import *

import textwrap
import os
import random

#Note: Video function is in userStories file

def clear_screen():
  if os.name == 'posix':  # For Unix/Linux/MacOS
        os.system('clear')
  elif os.name == 'nt':  # For Windows
        os.system('cls')

random_number = random.randint(0, 2)
  
def startupLanding():
    #clear_screen()
    # Comment this code chunk out before submission
    testimonialStory()
    # Up to this point needs to be commented out before submission
    """
    #User stories
    cursor.execute("SELECT story FROM stories")
    userStory = cursor.fetchall()
  
    print("Testimonial")
    storyImport = userStory[random_number]
    storyText = storyImport[0]
    wrapped_story = textwrap.fill(storyText, width=80)
    print(wrapped_story)
    print("\n")
    """
    
    # User menu
    print("Welcome to inCollege: inCollege is your")
    print("Login: (1)")
    print("Sign up: (2) ")
    print("Delete Users: (3)")
    print("Look up a user: (4)")
    print("Watch Video: (5)")

    uInput = int(input("Please select either 1, 2, 3, 4, or 5 based on which option you would like to do: "))

    # Once option is picked we then will choose which function that needs to be done
    if uInput == 1:
        UserLogin()
    elif uInput == 2:
        createUser()
    elif uInput == 3:
        deleteUser()
    elif uInput == 4:
        searchUser()
    elif uInput == 5:
      videoPlay()
    else:
        print("Invalid option")