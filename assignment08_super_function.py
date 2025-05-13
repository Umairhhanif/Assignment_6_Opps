class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the base class
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")


teacher1 = Teacher("Mohammad Umair", "Computer Science")
teacher1.display() 