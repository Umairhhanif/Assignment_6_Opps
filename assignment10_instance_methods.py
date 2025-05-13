class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof! I am a {self.breed}.")

dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark() # Output: Buddy says Woof! I am a Golden Retriever.