
class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 1
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print("Number of pages:", self.__number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 1
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print("Issue number:", self.__issue_number)


# Two Publication objects
publication1 = Publication("Library News", "Alex Cruz")
publication2 = Publication("Reading Guide", "Maria Santos")

# Two Book objects
book1 = Book("Noli Me Tangere", "Jose Rizal", 400)
book2 = Book("The Little Prince", "Antoine de Saint-Exupery", 96)

# Two Magazine objects
magazine1 = Magazine("Science Today", "John Reyes", 12)
magazine2 = Magazine("National Geographic", "Sarah Lee", 25)


# Display Publication information
print("=== PUBLICATIONS ===")
publication1.display_info()
print()
publication2.display_info()

# Display Book information
print("\n=== BOOKS ===")
book1.display_info()
print()
book2.display_info()

# Display Magazine information
print("\n=== MAGAZINES ===")
magazine1.display_info()
print()
magazine2.display_info()

