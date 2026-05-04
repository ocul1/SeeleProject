import os
import datetime

writerDeck_DIR = "writerDeck"

def ensure_journal_dir():
    if not os.path.exists(writerDeck_DIR):
        os.makedirs(writerDeck_DIR)

def greeting():
    print("Hello!, Welcome to the WriterDeck Program by ocul1")
    print()
greeting()

def name_gathering():
    name = input("Name of person submitting entry: ")
    print()
name_gathering()

def writer_deck_main():
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


