from Author import Author
from Book import Book

def main():
    try:
        options1 = "\n\n 1) Create author \n 2) List authors \n 3) Update author \n 4) Delete author"
        options2 = "\n 5) Create book \n 6) List books \n 7) Update book \n 8) Delete book \n 0) Exit"
        print("\nChoose an option:", options1, options2)
        op = int(input())

        if op == 0:
            SystemExit(0)
        elif op == 1:
            createAuthor()
        elif op == 2:
            listAuthors()
        elif op == 3:
            updateAuthor()
        elif op == 4:
            deleteAuthor()
        elif op == 5:
            createBook()
        elif op == 6:
            listBooks()
        elif op == 7:
            updateBook()
        elif op == 8:
            deleteBook()
        else: 
            print("\nYou probably typed a letter wwhere a number is expected. Try again...")
            main()
    except:
        print("\nYou probably typed a letter wwhere a number is expected. Try again...")
        main()

def getId():
    #To be used at update and delete
    print("\n Type the id to proceed: ")
    id = int(input())
    return id

#------------------------------Authors----------------------------
authorsArr = []

def createAuthor():
    print("\nType the author's id: ")
    authorId = int(input())

    print("\nType the author's name: ")
    authorName = input()

    authorsArr.append(Author(authorId, authorName))
    print("Author successfully created!")

    main()
    
def listAuthors():
    print('\nAuthors: ')
    for author in authorsArr:
        print(f"  Author's id: {author.authorId} Author's name: {author.authorName}")
    
    main()

def updateAuthor():
    id = getId()

    for author in authorsArr:
        if author.authorId == id:
            print("\nWhat do you want do update? \n 1) Author's id \n 2) Author's name")
            toUpdate = int(input())

            print("Type the new value: ")
            newValue = input()

            if toUpdate == 1:
                author.authorId = int(newValue)
                print("Author's id successfully updated!")
            elif toUpdate == 2:
                author.authorName = newValue
                print("Author's name successfully updated!")

    main()

def deleteAuthor():
    id = getId()

    for author in authorsArr:
        if author.authorId == id:
            authorsArr.remove(author)
            print("\n Successfully removed!")
    
    main()

#------------------------------Books----------------------------

booksArr = []

def createBook():
    print("Type the book's id: ")
    bookId = int(input())

    print("Type the book's name: ")
    bookName = input()

    print("Type the author's Id: ")
    authorId = int(input())

    for author in authorsArr:
        if author.authorId == authorId:
            booksArr.append(Book(bookId, bookName, author.authorId, author.authorName))
            print("Book created!")

    main()


def listBooks():
    print('\nBooks:')
    for book in booksArr:
        print(f"  Book id: {book.bookId} Book name: {book.bookName} Author id: {book.authorId} Author name: {book.authorName}")

    main()

def updateBook():
    id = getId()

    print("What to change? \n 1) Book id \n 2) Book name \n 3) Book author")
    operation = int(input())

    print("Type the new value: ")
    newValue = input()
#
    if type(operation) == int and operation > 0 and operation < 4:
        for book in booksArr:
            if book.bookId == id:
                if operation == 1:
                    book.bookId = int(newValue)
                elif operation == 2:
                    book.bookName = newValue
                elif operation == 3: 
                    for author in authorsArr:
                        if author.authorId == int(newValue):
                            book.authorId = author.authorId
                            book.authorName = author.authorName
                print("\nBook has been updated!")

    else:
        print("\nChoose a valid option next time...")

    main()


def deleteBook():
    id = getId()

    for book in booksArr:
        if book.bookId == id:
            booksArr.remove(book)
            print("Book removed!")

    main()

main()