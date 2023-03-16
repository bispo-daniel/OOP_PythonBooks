from Book import Book
from Author import Author

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

#------------------------------Authors----------------------------

authorsArr = []

def getAuthorId():
    #To be used at update and delete
    print("\n Type the author's id to proceed: ")
    id = int(input())
    return id

def createAuthor():
    print("\nType the author's id: ")
    authorId = int(input())

    print("\nType the author's name: ")
    authorName = input()

    authorsArr.append(Author(authorId, authorName))

    main()
    
def listAuthors():
    for author in authorsArr:
        print("Author's id:", author.authorId, " Author's name:", author.authorName)
    
    main()

def updateAuthor():
    id = getAuthorId()

    for author in authorsArr:
        if author.authorId == id:
            print("\nWhat do you want do update? \n 1) Author's id \n 2) Author's name")
            toUpdate = int(input())

            print("Type the new value: ")
            newValue = input()

            if toUpdate == 1:
                author.authorId = int(newValue)
            elif toUpdate == 2:
                author.authorName = newValue

    main()

def deleteAuthor():
    id = getAuthorId()

    for author in authorsArr:
        if author.authorId == id:
            authorsArr.remove(author)
            print("\n Successfully removed!")
    
    main()

#------------------------------Books----------------------------

booksArr = []

def createBook():
    return ''
def listBooks():
    return ''
def updateBook():
    return ''
def deleteBook():
    return ''

main()