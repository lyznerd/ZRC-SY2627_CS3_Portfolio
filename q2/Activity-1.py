# 1. Public
# A GameCharacter class has a username that can be displayed and accessed by anyone.
class GameCharacter:
    def __init__(self, username):
        self.username = username

# 2. Private
# A BankAccount class has a balance that shouldn't be accessed directly outside the class.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

# 3. Protected
# A Vehicle class has an engineCode that should only be accessed within the class and its subclasses.
class Vehicle:
    def __init__(self, engineCode):
        self._engineCode = engineCode

# 4. Public
# A Student class has a schoolName that is safe for everyone to view and modify.
class Student:
    def __init__(self, schoolName):
        self.schoolName = schoolName

# 5. Private
# A VotingSystem class has a voterID that must be hidden for security reasons.
class VotingSystem:
    def __init__(self, voterID):
        self.__voterID = voterID
