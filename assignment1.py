"""
Name: Joshua Timothy Gratio Wibowo
Date started: 17/4/2022
Description: Program to track user books that are required ro be read and books
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
    user_input = check_input(user_input)  # error checking
    while user_input != MENU_CHOICES[3]:  # while loop with "Q" as exit condition
        if user_input == MENU_CHOICES[0]:  # if user input "L"
            required_book = list_all_books(book_list)
            print_all_books(book_list, required_book)
            print_menu()
            user_input = get_input()
            user_input = check_input(user_input)
        elif user_input == MENU_CHOICES[1]:  # if user input "A"
            book_list = add_new_book(book_list)
            print_menu()
            user_input = get_input()
            user_input = check_input(user_input)
        elif user_input == MENU_CHOICES[2]:  # if user input "M"
            book_list = mark_book(book_list)
            print_menu()
            user_input = get_input()
            user_input = check_input(user_input)
    overwrite_data(book_data, book_list)
    print(f"{len(book_list)} books saved to books.csv")
    print("So many books, so little time. Frank Zappa")

    book_data.close()  # close books.csv


def overwrite_data(book_data, book_list):
    """Overwrite old data with new data"""
    book_data.seek(0)
    for book in range(len(book_list)):
        for item in range(len(book_list[book])):
            if item == len(book_list[book]) - 1:
                book_data.write(f"{book_list[book][item]}")
            else:
                book_data.write(f"{book_list[book][item]},")
        if book != len(book_list) - 1:
            book_data.write("\n")
    book_data.truncate()


def mark_book(book_list):
    """Mark book sub program"""
    required_book = list_all_books(book_list)
    if len(required_book) > 0:
        print_all_books(book_list, required_book)
        print("Enter the number of a book to mark as completed")
        book_number = book_number_check(book_list)
        book_list = check_if_completed(book_list, book_number, required_book)
    else:
        print("No required books")
    return book_list


def check_if_completed(book_list, book_number, required_book):
    if book_list[book_number] in required_book:
        required_book.remove(book_list[book_number])
        book_list[book_number][3] = COMPLETED
        print(f"{book_list[book_number][0]} by {book_list[book_number][1]} completed!")
    else:
        print("That book is already completed")
    return book_list


def book_number_check(book_list):
    """Check if the page input is valid"""
    while True:
        book_num = input(">>> ")
        try:
            book_num = int(book_num)
            while int(book_num) <= 0:
                print("Number must be > 0")
                book_num = input(">>> ")
            while int(book_num) > len(book_list):
                print("Invalid book number")
                book_num = input(">>> ")
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    return int(book_num) - 1


def add_new_book(book_list):
    """Add new book sub program"""
    book_title = input("Title: ")
    book_title = not_blank(book_title)
    book_author = input("Author: ")
    book_author = not_blank(book_author)
    book_page = page_check()
    book_list.append([book_title, book_author, book_page, REQUIRED])
    book_list = sorted(book_list, key=lambda x: (x[1], x[0]))
    print(f"{book_title} by {book_author}, ({book_page} pages) added to Reading Tracker")
    return book_list


def page_check():
    """Check if the page input is valid"""
    while True:
        book_page = input("Pages: ")
        try:
            book_page = int(book_page)
            while int(book_page) <= 0:
                print("Number must be > 0")
                book_page = input("Pages: ")
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    return book_page


def not_blank(user_input):
    """Check if an input is blank or not"""
    while user_input == "" or user_input.isspace():
        print("Input can not be blank")
        user_input = input("Title: ")
    return user_input


def list_all_books(book_list):
    """List all books sub program"""
    required_book = check_required(book_list)
    return required_book


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
    if len(required_book) == 0:
        print("No books left to read. Why not add a new book?")
    else:
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
    book_list = sorted(book_list, key=lambda x: (x[1], x[0]))
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
