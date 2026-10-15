class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")

class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages):
        if isinstance(number_pages, int) and not isinstance(number_pages, bool) and number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print("The number of pages must be positive")

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.__number_of_pages}")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if isinstance(issue_number, int) and not isinstance(issue_number, bool) and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive")

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")

publications = []
books = []
magazines = []

print("LIBRARY MANAGEMENT SYSTEM")

for i in range(2):
    print(f"\nEnter Publication {i + 1} Information")
    title = input("Enter title: ")
    author = input("Enter author: ")
    publications.append(Publication(title, author))

for i in range(2):
    print(f"\nEnter Book {i + 1} Information")
    title = input("Enter title: ")
    author = input("Enter author: ")

    while True:
        try:
            number_pages = int(input("Enter number of pages: "))
            if number_pages > 0:
                break
            print("The number of pages must be positive")
        except ValueError:
            print("Please enter a valid whole number")

    books.append(Book(title, author, number_pages))

for i in range(2):
    print(f"\nEnter Magazine {i + 1} Information")
    title = input("Enter title: ")
    author = input("Enter author: ")

    while True:
        try:
            issue_number = int(input("Enter issue number: "))
            if issue_number > 0:
                break
            print("The issue number must be positive")
        except ValueError:
            print("Please enter a valid whole number")

    magazines.append(Magazine(title, author, issue_number))

print("\n===== PUBLICATIONS =====")
for publication in publications:
    publication.display_info()
    print()

print("===== BOOKS =====")
for book in books:
    book.display_info()
    print()

print("===== MAGAZINES =====")
for magazine in magazines:
    magazine.display_info()
    print()

