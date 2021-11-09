
import threading

class rectangle():
    def __init__(self, breadth, lenght):
        self.breadth = breadth
        self.lenght = lenght
        
    def area(self):
        return self.breadth * self.lenght

a = int(input("Enter lenght of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = rectangle(a, b)
print("Area of rectangle:", obj.area())

print()
