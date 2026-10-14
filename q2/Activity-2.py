
#Activity 2: Getters, Setters, and Deleters

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # getter methods
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # setter methods
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be more than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Height must be more than zero")

    # deleter methods
    @width.deleter
    def width(self):
        del self.__width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self.__height
        print("Height has been deleted")


# test
rect = Rectangle(10, 5)

# Reading some attributes
print(f"Width: {rect.width}")
print(f"Height: {rect.height}")

rect.width = 15
rect.height = 20

print(f"Updated Width: {rect.width}")
