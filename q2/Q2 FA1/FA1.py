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

publication1 = Publication("Introduction to Python", "John Smith")
publication2 = Publication("Computer Science Basics", "Mary Johnson")

book1 = Book("Python Programming", "Mark Lee", 350)
book2 = Book("Data Structures", "Anna Cruz", 280)

magazine1 = Magazine("Science Today", "Peter Brown", 12)
magazine2 = Magazine("Tech Monthly", "Lisa Garcia", 8)

print("===== PUBLICATIONS =====")
publication1.display_info()
print()
publication2.display_info()

print("\n===== BOOKS =====")
book1.display_info()
print()
book2.display_info()

print("\n===== MAGAZINES =====")
magazine1.display_info()
print()
magazine2.display_info()
```

# Display Magazine information
print("\n=== MAGAZINES ===")
magazine1.display_info()
print()
magazine2.display_info()

