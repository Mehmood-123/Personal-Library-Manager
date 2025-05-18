import os
import json

# File to store the library
LIBRARY_FILE = "library.txt"

# Load library from file if it exists
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book to the library
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_input == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for books by title or author
def search_books(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        term = input("Enter the title: ").strip().lower()
        results = [book for book in library if term in book["title"].lower()]
    elif choice == "2":
        term = input("Enter the author: ").strip().lower()
        results = [book for book in library if term in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if results:
        print("\nMatching Books:")
        for i, book in enumerate(results, 1):
            display_book(book, i)
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.")
        return
    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        display_book(book, i)

# Helper to print a single book
def display_book(book, index):
    read_status = "Read" if book["read"] else "Unread"
    print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Show statistics
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("Your library is empty.")
        return
    read_count = sum(book["read"] for book in library)
    percentage_read = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage_read:.1f}%")

# Main menu system
def main():
    library = load_library()
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
