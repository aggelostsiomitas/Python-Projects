import json 
import os 

# this code is a simple implementation of a library management system
# the user is able to see the books that are available in the library , 
# to add a book on the system and borrow it or return it if the
# necessary conditions are meant (if the book is available or not) 



# file 
FILE="python/library.json"


#data handling function
def load_library():
    # if the file does not exist throw an error
    if not os.path.exists(FILE):
        return []
    with open(FILE,"r") as f:
        return json.load(f)
    

#save the library 
def save_library(books):
    with open(FILE,"w") as f:
        json.dump(books,f,indent=2)
    

#display the books function
def show_books(books):
    #id there are not books to show 
    if not books:
        print("there are no books to show ")
        return 
    
    #if there are books 
    for i, b in enumerate(books): 
        status = "Available" if not b["borrowed"] else f"Borrowed by {b['borrower']}" 
        print(f"{i+1}. {b['title']} by {b['author']} ({status})")


#add book function 
def add_book(books):
    title=input("give me the title of the book ")
    author=input("give me the name of the author of the book ")

    #if no title or author throw error
    if not title or not author:
        print("invalid input")
        return 

    #append the new book 
    books.append({
        "title":title,
        "author":author,
        "borrowed":False,
        "borrower": ""
    }) 

    print("book added successfully")

    #save the changes in library 
    save_library(books)
    


#remove book function
def remove_book(books):
    show_books(books)

    idx=int(input("which books do you want to remove ?"))-1

    if idx<0:
        print("invalid input ")
    books.pop(idx)
    print("book removes successfuly")
    save_library(books)



#boorow book function
def borrow_book(books): 
    show_books(books) 
    try: 
        idx = int(input("Which book do you want to borrow? ")) - 1 
        if idx < 0 or idx >= len(books): 
            print("Invalid index.") 
            return 
        if books[idx]["borrowed"]: 
            print("Book is already borrowed.") 
            return
        name = input("Borrower name: ").strip() 
        books[idx]["borrowed"] = True 
        books[idx]["borrower"] = name 
        print(f"Book borrowed successfully by {name}.")
        save_library(books) 
    except: 
        print("Invalid input.")



#return book  function
def return_books(books):
    show_books(books)

    try:
        idx=int(input("which book do you wanrt to return ?"))-1

        if not books[idx]["borrowed"]:
            print("books is not borrowed")
            return 
        
        books[idx]["borrowed"]=False
        books[idx]["borrower"]=""

        print("books successfuly returned ")
        save_library(books)

    except :
        print("invalid input ")



#search for a book function
def search_book(books):
    #search the books based on keywords
    key=input("search keyword :").strip().lower()

    #if some key exists in either title or author word then show it
    results=[b for b in books if  key in b["title"].lower() or key in b["author"].lower()]

    print("\nHere are the search results ")
    show_books(results)


#menu 
def menu():
    print("\n ========= Library system ===========")
    print("1. Show all books")
    print("2.Add book")
    print("3.Remove book")
    print("4. Borrow book")
    print("5. Return book ")
    print("6. Search book")
    print("7.Exit")


#main function 
def main():
    books=load_library()

    while True:
        menu()
        choice=input("Choose :").strip()
        if choice=="1":
            show_books(books)
        elif choice=="2":
            add_book(books)
        elif choice=="3":
            remove_book(books)
        elif choice=="4":
            borrow_book(books)
        elif choice=="5":
            return_books(books)
        elif choice=="6":
            search_book(books)
        elif choice=="7":
            print("thank you for visiting us")
            break
        else :
            print("invalid input ")
main()