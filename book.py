#Creating class of book for storing title and author

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="book",
    )



class BookManager:
    def __init__(self):
        pass
    
    def add_book(self, title, author): #function of adding book
        #book = Book(title, author) #creating an instance of class book by passing two arguments
        try:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM book.book")
            results = mycursor.fetchall()
            for row in results:
                if row[0].strip() == title and row[1].strip() == author:
                    print("Book is already present")
                    return
            sql= "INSERT INTO book.book (title, author) VALUES (%s, %s)"
            val = (title, author)
            mycursor.execute(sql, val)
            mydb.commit()
            #self.books.append(book) #appending book in self.book list created
            print("Book added successfully.")
        except mysql.connector.Error as error:
            print(error)
        finally:
            mycursor.close()

    def remove_book(self, title): #function of removing book
        try:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM book.book")
            results = mycursor.fetchall()
            if not results:
                print("No Book is Found")
                return
            for row in results:
                if row[0].strip() == title:
                    print(row[0])
                    sql="DELETE FROM book.book WHERE title=%s"
                    val=(title,)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("Book Deleted Successfully")
                    return
        except mysql.connector.Error as error:
            print(error)
        finally:
            mycursor.close()


    def display_books(self): #function of displaying book
        try:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM book.book")
            results = mycursor.fetchall()
            if not results:
                print("No Book is Found")
            else:
                for row in results:
                    print(f"Title: {row[0].strip()}, Author: {row[1].strip()}")
        except mysql.connector.Error as error:
            print(error)
        finally:
            mycursor.close()


    def search_book(self, title): #function of searching book with title parameter
        found = False
        try:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM book.book")
            results = mycursor.fetchall()
            for row in results:
                if row[0].strip() == title:
                    print(f"Title: {row[0]}, Author: {row[1]}")
                    found = True
            if not found: # if not present then then print book not found
                print("Book not found.")
        except mysql.connector.Error as error:
            print(error)
        finally:
            mycursor.close()
        


def main():
    book_manager = BookManager() #Storing Object instance of book manager in variable
    while True:  #Running infinity loop
        print("Welcome to the Book Management System!")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter your choice: ") #Based on the data provided user will choose an option and it will store in variable choice 
        #The condition will execute based on the data variable choice
        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            book_manager.add_book(title, author) #Utilizing the function which was create in Book_Manager class and passing two argument to add the book in list

        elif choice == '2':
            title = input("Enter the title of the book to be removed: ")
            book_manager.remove_book(title)

        elif choice == '3':
            book_manager.display_books()

        elif choice == '4':
            title = input("Enter the title of the book to be searched: ")
            book_manager.search_book(title)

        elif choice == '5':
            print("Thank you for using the Book Management System!")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == '__main__': #It will execute first since the condition is true
    main() # the main function is called
    
