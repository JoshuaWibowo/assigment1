"""
Name: Joshua Timothy Gratio Wibowo
Date started: 17/4/2022
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-JoshuaWibowo
"""

MENU_CHOICES = ("L", "A", "M", "Q")


def main():
    """Main function"""
    book_data = open("books.csv", "r")  # open books.csv
    print("Reading Tracker 1.0 - by Joshua Wibowo")
    print_total_book(book_data)
    print_menu()
    user_input = get_input()

    book_data.close()


def get_input():
    """Get user input"""
    user_input = input(">>> ")
    user_input = user_input.lower()
    return user_input


def print_menu():
    """Print menu"""
    print("Menu:"
          f"{MENU_CHOICES[0]} - List all books"
          f"{MENU_CHOICES[1]} - Add new book"
          f"{MENU_CHOICES[2]} - Mark a book as completed"
          f"{MENU_CHOICES[3]} - Quit")


def print_total_book(book_data):
    """Print total book in the data"""
    print(f"{len(book_data.readlines())} books loaded")


if __name__ == '__main__':
    main()
