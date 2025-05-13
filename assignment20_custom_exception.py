class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    """Check if the provided age is valid (18 or older)."""
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    return True

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e.message}")
except ValueError:
    print("Invalid input. Please enter a number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")