"""
Name: Joshua Timothy Gratio Wibowo
Date started: 17/4/2022
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-JoshuaWibowo
"""

MENU_CHOICES = ("L", "A", "M", "Q")


def main():
    """Main function"""
    book_data = open("books.csv", "r")  # open books.csv
    book_list = store_to_list(book_data)
    print("Reading Tracker 1.0 - by Joshua Wibowo")
    print_total_book(book_list)
    print_menu()
    user_input = get_input()
    user_input = check_input(user_input)
    while user_input != MENU_CHOICES[3]:
        print("test")

    book_data.close()


def store_to_list(book_data):
    """store book data into a list of list"""
    books = book_data.read().split("\n")
    book_list = []
    for i in range(len(books)):
        book_list.append(books[i].split(","))
    return book_list


def check_input(u_input):
    """Check if input is valid"""
    while u_input not in MENU_CHOICES:
        print("Invalid choice")
        print_menu()
        u_input = get_input()
    return u_input


def get_input():
    """Get user input"""
    user_input = input(">>> ")
    user_input = user_input.upper()
    return user_input


def print_menu():
    """Print menu"""
    print("Menu:"
          f"\n{MENU_CHOICES[0]} - List all books"
          f"\n{MENU_CHOICES[1]} - Add new book"
          f"\n{MENU_CHOICES[2]} - Mark a book as completed"
          f"\n{MENU_CHOICES[3]} - Quit")


def print_total_book(book_data):
    """Print total book in the data"""
    print(f"{len(book_data)} books loaded")


if __name__ == '__main__':
    main()
