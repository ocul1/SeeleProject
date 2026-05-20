import os
import datetime

writerDeck_DIR = "writerDeck"

def ensure_writerDeck_dir():
    if not os.path.exists(writerDeck_DIR):
        os.makedirs(writerDeck_DIR)
        

def greeting():
    print("Hello!, Welcome to the WriterDeck Program by ocul1")
    print()
    

def writer_deck_main():
    today = datetime.date.today()
    print(today)
    name = input("Name of person submitting entry: ")
    print()
    print("Author of Entry: ", name)
    print(today)
    title = input("Entry Title: ")
    print("Write your entry, and type 'END' on a new line to finish")
    print()
    print(title)
    print()
    print("----------------")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    saving_text(lines,name,today,title)

#MISSING SAVE TO FILE HERE
def saving_text(lines, name, today, title):
    file_path = os.path.join(writerDeck_DIR, "writerdeck.txt")
    with open(file_path,"a",encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%I:%M %p")
        file.write("Author: " + name + "\n")
        file.write("Title: " + title + "\n")
        file.write("Date: " + str(today)+ "\n")
        file.write("Time: " + timestamp + "\n")
        file.write("\n".join(lines))
        file.write("\n"+"-" * 40 + "\n")
        

def run_again():
    answer = input("Would you like to run this program again, 'Y' or 'N': ").lower()    
    while answer not in ("y", "n"):
        answer = input("Input Error: Please enter y or n: ").lower()
    if answer == 'y':
        return True
    else:
        return False 
    

main_core = True
while main_core ==True:
    ensure_writerDeck_dir()
    greeting()
    writer_deck_main()
    main_core = run_again()

    
    