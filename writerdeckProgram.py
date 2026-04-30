def greeting():
    print("Hello!, Welcome to the WriterDeck Program by ocul1")
    print()
greeting()

def name_gathering():
    name = input("Name of person submitting entry: ")
    print()
name_gathering()

def writer_deck_main():
    



def run_again():
    answer = input("Would you like to run this program again, 'Y' or 'N': ").lower()    
    while answer not in ("y", "n"):
        answer = input("Input Error: Please enter y or n: ").lower()
    if answer == 'y':
        return True
    else:
        return False 


