class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation

    def show(self):
        print(f"Department: {self.dept_name}")
        self.employee.show()

# Independent Employee object
emp = Employee("Ali")

# Department takes an existing Employee object
dept = Department("HR", emp)

dept.show()  # Output: Department: HR Employee Name: Ali