def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        return f"Person Name: {self.name}"
    
person = Person("Mohammad Umair")
print(person.greet())  
print(person.show()) 
# Output:
# Hello from Decorator!