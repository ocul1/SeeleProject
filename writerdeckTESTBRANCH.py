import os
import datetime

writerDeck_DIR = "writerDeck"

def ensure_writerDeck_dir():
    if not os.path.exists(writerDeck_DIR):
        os.makedirs(writerDeck_DIR)
        
ensure_writerDeck_dir()

def greeting():
    print("Hello!, Welcome to the WriterDeck Program by ocul1")
    print()
    
greeting()
    
name_gathering()

def writer_deck_main():
    name = input("Name of person submitting entry: ")
    print()
    print("Author of Entry: ", name)
    title = input("Entry Title: ")
    print("Write your entry, and type 'END' on a new line to finish")
    print(title)
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    
writer_deck_main()
    

def run_again():
    answer = input("Would you like to run this program again, 'Y' or 'N': ").lower()    
    while answer not in ("y", "n"):
        answer = input("Input Error: Please enter y or n: ").lower()
    if answer == 'y':
        return True
    else:
        return False 
    
run_again()


