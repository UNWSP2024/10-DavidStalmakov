# David Stalmakov, 11/5/2025
# Triangle Perimeter
# The programming task at the end of the first video about OOP
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
# Create the object
t1 = Triangle(26, 14, 13)
# Display
print("Perimeter of the triangle:", t1.perimeter())