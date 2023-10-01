### External Files ###
from UI import *
from generalLinks import *

def usefulLinksMenu():
    exitInput = 0
    while exitInput == 0:
        spacer()
        header('Useful Links')
        print("(1)  General")
        print("(2)  Browse inCollege")
        print("(3)  Business Solutions")
        print("(4)  Directories")

        uInput = input("Input Selection (Q to quit and return): ")

        if uInput == '1':
            generalLinksMenu()
        elif uInput == '2':
            browseApp()
        elif uInput == '3':
            busSolutions()
        elif uInput == '4':
            directory()
        elif uInput == 'Q' or uInput == 'q':
            exitInput = 1
            spacer()
        else:
            print("Invalid Option Try Again")


def browseApp():
    print("under construction")
    return

def busSolutions():
    print("under construction")
    return

def directory():
    print("under construction")
    return
