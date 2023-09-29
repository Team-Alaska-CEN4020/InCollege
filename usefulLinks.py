### External Files ###
from UI import *

def usefulLinksMenu():
    exitInput = 0
    while exitInput == 0:
        spacer()
        header('Useful Links')
        print("(1)  General")
        print("(2)  Browse inCollege")
        print("(3)  Business Solutions")
        print("(4)  Directories")
        print("(0)  Return")

        uInput = input("Input Selection (Q to quit): ")

        if uInput == '1':
            general()
        elif uInput == '2':
            browseApp()
        elif uInput == '3':
            busSolutions()
        elif uInput == '4':
            directory()
        elif uInput == '0':
            return
        elif uInput == 'Q' or 'q':
            exitInput = 1
            spacer()
        else:
            print("Invalid Option Try Again")
            spacer()

def general():
    print("under construction")
    return

def browseApp():
    print("under construction")
    return

def busSolutions():
    print("under construction")
    return

def directory():
    print("under construction")
    return