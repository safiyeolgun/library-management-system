import os
from time import sleep
#import pandas as pd
"""
class Library:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    
    def list_books(self):
        pass
    
    def add_book(self):
        pass

    def remove_book(self):
        pass


def control(value, val=0):
    message = [".","/number or one name.", " or invalid year term.", " or invalid page number."]
    if value == 1:
        print("{:>30}".format(u"\u2714"))
    else:
        print("{:>30}".format(u"\u274c"))
        print("{:>30}{}\n {:>30}".format("You have entried blank",message[val],"Please entry a valid."))
        
"""
    
"""
def check_title():
    while True:
        title = input("Enter the book title: ").strip()
        if not re.match(r"^[0-9a-zA-Z]+(?: [0-9a-zA-Z]+)*$", title):        
        #not title:
            control(0,0)            
        else:
            title = re.sub(r"\s+"," ", title)
            control(1)            
            return title.title()

def check_author():
    while True:
        author = input("Enter the author: ").strip().lower()
        if not re.match(r"^(?:[a-zıçşöü]{2,}\s{1,}){1,}[a-zıçşöü]{2,}$", author):        
            control(0,1)            
        else:
            author = re.sub(r"\s+", " ", author)
            control(1)
            return author.title()

def check_year():
    while True:
        year = input("Enter the release year: ").strip()
        if not re.match(r"[12]{1}[0-9]{3}", year):            
            control(0,2)            
        else:
            control(1)
            return year
        
def check_pages():    
    while True:
        pages = input("Enter the number of pages: ").strip()
        if not re.match(r"[1-9]{1}[0-9]{0,}", pages):
            control(0,3)
        else:
            control(1)
            return pages
"""




def clear():
    #if os.system("clear"): os.system("cls")    
    print("\033[H\033[J") 


def add_book():
            #title = check_title()   
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the release year: ")
    pages = input("Enter the number of pages: ")
    line = title + "," + author + "," + year + "," + pages + "\n"
    try:
        file = open("book.txt", "a+")
        #print("file opened")
    except:
        file = open("book.txt", "w")
        #print("file created")

    finally:
        file.write(line)
        file.close()


def list_books():
    clear()
    try:
        #file = open("book.txt", "r")
        os.path.exists("book.txt")           
    
    except FileNotFoundError:
        print("File not found.")        
    else:
        print("{:<5} {:<40} {:<25} {:<15} {:<10}".format("No", "Title", "Author", "Release Year", "Pages"))
        print("*"*100)
        record = 0
        with open("book.txt") as file:     
            for line in file:     
                record += 1 
                cell = line.strip().split(",")
                print("{:<5} {:<40} {:<25} {:<15} {:<10}".format(record, cell[0], cell[1], cell[2], cell[3]))
                if (record%20) == 0:
                    input("\n{:>100}".format("If you want to next 20 record press <enter>"))
                    #print("slip")
                    print("\033[H\033[J") 
                    print("....")
                    print("{:<5} {:<40} {:<25} {:<15} {:<10}".format("No", "Title", "Author", "Release Year", "Pages"))
                    print()
                    print("*"*100)
     
        file.close()
     
        #df = pd.read_csv("book.txt", header=None, names= ["Title", "Author", "Release Year", "Pages"], sep=",", encoding = "latin-1")
        #print(df)

def remove_book():
    record = 0
    with open("book.txt") as file:
        for line in file:  
            record += 1
        
    print(record)

    file.close()
               

"""
def get_lines(file_name: str) -> [str]:   
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines


lines = get_lines('book.txt')
for i in lines:
    
    print(i[:-1])

"""
def menu ():
    while True:
        clear()        

        print('''
*** MENU ***
1) List Books
2) Add Book
3) Remove Book
q) Quit
        ''')
        select = input("Enter your choice (1-3/q):")
        if select == "1":
            list_books()           
            #input("\n{:>100}".format("Press <enter> to return main menu"))
            sleep(5)
        elif select == "2":
            add_book()           
            #input("\n{:>100}".format("New book has been added. Press <enter> to return main menu"))
            #print("\n{:>100}".format("New book has been added."))
            sleep(5)
        elif select == "3":
            remove_book()
            print("3 Ok")
            sleep(5)
        elif select in ["q", "Q"]:
            print("Programme is being closed...")            
            break
        else:            
            input("\nPlease select from menu... !\nPress <enter> to return main menu")

menu()


