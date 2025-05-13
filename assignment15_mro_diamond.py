class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    def show(self):
        print("Class D")
        super().show()  # Calls the show method of the first parent class in MRO

# Create an object of D

a = A()
b = B()
c = C()
d = D()

# Call show() to observe MRO
a.show()
b.show()
c.show()
d.show()
print(D.mro())  # Method Resolution Order