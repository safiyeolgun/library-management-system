import os, math, re
from time import sleep

class Library:

# constructer method 
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
    
    def __str__(self):
        return f"{self.title},{self.author},{self.year},{self.pages}"   

    # destructor method 
    def __del__(self):
        pass


def clear():
    #if os.system("clear"): os.system("cls")    
    print("\033[H\033[J")       


def control(value):
    entry_message = ["book title", "author", "release year", "number of pages"]
    message = [".","/number or one name.", " or invalid year term.", " or invalid page number."]
    patern =[r"^[0-9a-zıçşöü]+(?: [0-9a-zıçşöü\s]+)*$", 
             r"^(?:[a-zıçşöü]{2,}\s{1,}){1,}[a-zıçşöü]{2,}$", 
             r"[12]{1}[0-9]{3}",             
             r"[1-9]{1}[0-9]{0,}"] 
    
    while True:
        entry = input(f"Enter the {entry_message[value]} : ").strip().lower() 
        if not re.match(patern[value], entry):
            print("{:>30}".format(u"\u274c"))
            print("{:>30}{}\n {:>30}".format("You have entried blank",message[value],"Please entry a valid."))
        else:
            entry = re.sub(r"\s+"," ", entry)
            print("{:>30}".format(u"\u2705"))            
            return entry.title()

def file_read():
    file = open("book.txt", "a+")
    file.seek(0)
    #lines = sorted(list(set(file.read().splitlines())))    
    lines = file.read().splitlines()
    file.close()
    return lines

def new():
        clear()
        title = control(0)
        author = control(1)
        year = control(2)
        pages = control(3)
        lib = Library(title, author, year, pages)
        return lib

def add_book(line):        
        lines = file_read()        
        try:            
            if lines.index(str(line)):
                print(u"\u274c", end =" ")                
                print("Your entries has been NOT recorded.")
                print("Sorry, there is at least one record containing this exact information.")            
                
        except: 
            file = open("book.txt", "a+")       
            file.write(str(line)+"\n")
            file.close()
            print(u"\u2705", end ="")
            print(" Your entries has been recorded.")
        sleep(5)        

def list_books():
    clear()
    lines = file_read()

    if len(lines)>=1:
        print("{:<5} {:<40} {:<25} {:<15} {:<10}".format("No", "Title", "Author", "Release Year", "Pages"))
        print("*"*100)
        page = 1
        for record, line in enumerate(lines,1):            
            #title, author, year, pages = line.strip().split(",")
            #print("{:<5} {:<40} {:<25} {:<15} {:<10}".format(record, title, author, year, pages))            
            lib = Library(*line.strip().split(","))            
            print("{:<5} {:<40} {:<25} {:<15} {:<10}".format(record, lib.title, lib.author, lib.year, lib.pages))
            del lib
            if (record % 20 == 0) & (record!=len(lines)):                
                print(f"\nPage: {page}/{math.ceil(len(lines)/20)}")                
                input("\n{:>100}".format("If you want to next records, press <enter>"))                
                clear()
                print("....")
                print("{:<5} {:<40} {:<25} {:<15} {:<10}".format("No", "Title", "Author", "Release Year", "Pages"))
                print()
                print("*"*100)
                page += 1
            
        print(f"\nPage: {page}/{math.ceil(len(lines)/20)}")  
    else:
         print("File has no record.")
    
    input("\n{:>100}".format("If you want to return main menu, press <enter>"))


def remove_book():
    lines = file_read()
    clear()
    if len(lines):
        title = []

        for line in lines:
            lib = Library(*line.strip().split(","))
            title.append(lib.title)
            del lib
        search = input("Please write full name of book which you want to remove from records: ").strip().title()

        try: 
            if title.index(search)>=0:            
                again = [str(index+1) + ":" + value for index, value in enumerate(lines) if value.split(",")[0] == search]
            
                print(f"There are {len(again)} books named <{search}>. All with exact information are listed below.\n")
                print("{:<5} {:<40} {:<25} {:<15} {:<10}".format("Index", "Title", "Author", "Release Year", "Pages"))
                print("*"*100)
                for line in again:
                    index, value = line.split(":")
                    lib = Library(*value.split(","))
                    print("{:<5} {:<40} {:<25} {:<15} {:<10}".format(index,lib.title, lib.author, lib.year, lib.pages))
                    del lib
             
                if len(again) > 1:
                    delete_index = input("\nPlease write index of book which you want to remove from records (A: All, C: Clear Books): ").strip().lower()

                    if delete_index =="c":                        
                        delete_index = [index for index, value in enumerate(lines)]
                        message = f" All books are removed from our records."                

                    elif delete_index =="a":
                        delete_index = [index for index, value in enumerate(lines)  if value.split(",")[0] == search]                    
                        message = f" All book named <{search}> are removed from our records."

                    else:
                        try:
                            if int(delete_index):                            
                                delete_index = [int(delete_index)-1]                            
                                message = f" Selected book named <{search}> is removed from our records."
                
                        except:
                            print("Wrong entry. Please valid entry")
                   

                else:
                    delete_index = [title.index(search)]
                    message = f" The book named <{search}> is removed from our records."
           
                select = input("\nAre you sure that you want to remove this book?(Yes: Y, No: N): ").strip().lower()
                if  select == "y":                
                
                    for line in reversed(delete_index):
                        lines.pop(line)

                    file = open("book.txt", "w")
                    for line in lines:
                        file.write(str(line)+"\n")
                    file.close()

                    print(u"\u2705", end ="")
                    print(message)                
                
                else:
                    print(u"\u274c", end ="")
                    print(" No record has been removed.")

        except:        
            print(u"\u274c", end ="")
            print(f" The book named <{search}> is NOT exited in our records.")
    else:        
        print("File has no record.")    
    input("\n{:>100}".format("If you want to return main menu, press <enter>")) 


def main():
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
        elif select == "2":            
            add_book(new())
        elif select == "3":            
            remove_book()                        
        elif select in ["q", "Q"]:
            print("Programme is being closed...")            
            sleep(3)
            break
        else:            
            print("\nyour selection from out of menu\nPlease select from menu... !") 
            sleep(3)

if __name__ == "__main__":
    main()

