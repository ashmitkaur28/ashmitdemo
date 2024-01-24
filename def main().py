def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            title = input("Enter the book title: ")
            author = input("Enter the author name: ")
            isbn = input("Enter the ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            print("Book added successfully!")

        elif choice == 2:
            isbn = input("Enter the ISBN of the book to remove: ")
            book = library.find_book_by_isbn(isbn)
            if book:
                library.remove_book(book)
                print("Book removed successfully!")
            else:
                print("Book not found.")

        elif choice == 3:
            library.display_books()

        elif choice == 4:
            isbn = input("Enter the ISBN of the book to borrow: ")
            book = library.find_book_by_isbn(isbn)
            if book and book.is_available:
                book.mark_as_borrowed()
                print("Book borrowed successfully!")
            else:
                print("Book not available for borrowing.")

        elif choice == 5:
            isbn = input("Enter the ISBN of the book to return: ")
            book = library.find_book_by_isbn(isbn)
            if book and not book.is_available:
                book.mark_as_available()
                print("Book returned successfully!")
            else:
                print("Invalid ISBN or book already available.")

        elif choice == 6:
            print("Exiting the Library Management System...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()