class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP is starting.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start(self):
        print(f"{self.brand} is starting.")
        self.engine.start()  


engine = Engine(150)

car = Car("Toyota", engine)

car.start()