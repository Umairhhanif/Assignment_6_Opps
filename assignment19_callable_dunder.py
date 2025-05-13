class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor
# Example usage
multiplier = Multiplier(3)
print(multiplier.factor) 
 
print(callable(multiplier))
print(multiplier(5))  
print(multiplier(10))  
print(multiplier.factor)