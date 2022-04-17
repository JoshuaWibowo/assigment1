"""
Name: Joshua Timothy Gratio Wibowo
Date started: 17/4/2022
Description: Program to track user books tat are required ro be readed and books
             they have completed.
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-JoshuaWibowo
"""

MENU_CHOICES = ("L", "A", "M", "Q")
COMPLETED = "c"
REQUIRED = "r"


def main():
    """Main function"""
    book_data = open("books.csv", "r+")  # open books.csv
    book_list = store_to_list(book_data)
    print("Reading Tracker 1.0 - by Joshua Wibowo")
    print_total_book(book_list)
    print_menu()
    user_input = get_input()
    user_input = check_input(user_input)
    while user_input != MENU_CHOICES[3]:  # while loop with "Q" as exit condition
        if user_input == MENU_CHOICES[0]:  # if user input "L"
            list_all_books(book_list)
            print_menu()
            user_input = get_input()
            user_input = check_input(user_input)

    book_data.close()  # close books.csv


def list_all_books(book_list):
    """List all books sub program"""
    required_book = check_required(book_list)
    print_all_books(book_list, required_book)


def print_all_books(book_list, required_book):
    """Print all the books and its data"""
    total_required_page = 0
    total_required_book = 0
    for book in range(len(book_list)):
        if book_list[book] in required_book:
            print(f"*{book + 1}. {book_list[book][0]:<38} by {book_list[book][1]:<17} {book_list[book][2]:>3} pages")
        else:
            print(f"{book + 1:>2}. {book_list[book][0]:<38} by {book_list[book][1]:<17} {book_list[book][2]:>3} pages")
    for book in required_book:
        total_required_page += int(book[2])
        total_required_book += 1
    print(f"You need to read {total_required_page} pages in {total_required_book} books.")


def check_required(book_list):
    """Check if book is required"""
    required_book = []
    for book in book_list:
        if book[3] == REQUIRED:  # check if it is "c" or "r"
            required_book.append(book)  # if it is required, add to required list
    return required_book


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
