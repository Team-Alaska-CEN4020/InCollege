def printTitle():
    """
    Prints the title in stylized ASCII characters.

    Parameters:
    None
    """
    print(" ")
    print("██╗          ██████╗ ██████╗ ██╗     ██╗     ███████╗ ██████╗ ███████╗")
    print("╚═╝██╗      ██╔════╝██╔═══██╗██║     ██║     ██╔════╝██╔════╝ ██╔════╝")
    print("██║███████╗ ██║     ██║   ██║██║     ██║     █████╗  ██║  ███╗█████╗  ")
    print("██║██║   ██╗██║     ██║   ██║██║     ██║     ██╔══╝  ██║   ██║██╔══╝  ")
    print("██║██║   ██║ ██████╗╚██████╔╝███████╗███████╗███████╗╚██████╔╝███████╗")
    print("╚═╝╚═╝   ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝")

def spacer():
    """
    Prints a bar that will be able to seperate information.

    Parameters:
    None
    """
    print(" ")
    print("███████████████████████████████████████████████████████████████████████╗")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print(" ")

def header(text: str):
    """
    Print the given text with a stylized underline
    
    Parameters:
    text (str): The text to be printed and underlined
    """
    print(text)
    print('═' * len(text))