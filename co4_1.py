#write a program to create a class rectangle with attribute length and breadth and methods to find area and perimeter.
class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*(self.breadth+self.length)

a=int(input("Enter Length Of 1st Rectangle:"))
b=int(input("Enter Breadth of 1st Rectangle:"))
obj=rectangle(a,b)

print("Area of 1st Rectangle:",obj.area())
print("Perimeter of 1st Rectangle:",obj.perimeter())

print()

c=int(input("Enter Length Of 2nd Rectangle:"))
d=int(input("Enter Breadth of 2nd Rectangle:"))
obj1=rectangle(c,d)

print("Area of 2nd Rectangle:",obj1.area())
print("Perimeter of 2nd Rectangle:",obj1.perimeter())

print()

if obj.area()> obj1.area():
    print("First Rectangle is Greater.")
elif obj.area() < obj1.area():
    print("Second Rectangle is Greater.")
else:
    print("Both Rectangle has equal are.")
