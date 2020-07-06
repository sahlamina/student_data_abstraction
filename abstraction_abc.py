from abc import *
# abc is how you begin using abstracton

# here i create a basic class called student
class Student:


    @abstractmethod
    def study(self):
        pass
    # the abstract method allows the child class to perform modifications