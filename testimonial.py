import random
import textwrap

from database import *
from UI import *


def testimonialStory():
    """
    Calculates how many stories are available, then picks a random one to display

    Parameters:
    None
    """
    header('Testimonials')
    # counts the number of stories than minus 1 so it can be used as a record index
    cursor.execute("SELECT COUNT(story) FROM stories")
    storyCount = cursor.fetchone()[0] -1  
    
    # generates a random number within the index range of stories
    randomStoryNum = random.randint(0, storyCount)
    
    # get and print the wrapped story found at the randomized index
    # the fetchall from the database returns a datatype of 'tuple' 
    # that we pull the 0th index of to get the actual text, then its wrapped
    cursor.execute("SELECT story FROM stories")
    storyQuery = cursor.fetchall()
    storyTuple = storyQuery[randomStoryNum]
    storyText = storyTuple[0]
    storyWrapped = textwrap.fill(storyText, width=80)
    print(storyWrapped)
    print("")
    spacer()