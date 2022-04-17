"""
Name: Joshua Timothy Gratio Wibowo
Date started: 17/4/2022
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-JoshuaWibowo
"""


def main():
    """Main function"""
    book_data = open("books.csv", "r")  # open books.csv
    print("Reading Tracker 1.0 - by Joshua Wibowo")
    print_total_book(book_data)
    print_menu()

    book_data.close()


def print_menu():
    print("Menu:\nL - List all books\nA - Add new book\nM - Mark a book as completed\nQ - Quit")


def print_total_book(book_data):
    """Print total book in the data"""
    print(f"{len(book_data.readlines())} books loaded")


if __name__ == '__main__':
    main()
