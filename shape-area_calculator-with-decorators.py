import math
from functools import wraps

def validate_dimensions(func):
    """Ensure all dimensions are positive"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        for attr, value in self.__dict__.items():
            if value <= 0:
                raise ValueError(f"{attr} must be positive, got {value}")
        return func(self, *args, **kwargs)
    return wrapper

def convert_to_cm2(func):
    """Convert area from m² to cm²"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        area_m2 = func(self, *args, **kwargs)
        area_cm2 = area_m2 * 10000
        print(f"[CONVERSION] Area in cm²: {area_cm2:.2f}")
        return area_m2
    return wrapper

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses mut implement the area method")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    @validate_dimensions
    @convert_to_cm2
    def area(self):
        return math.pi*self.radius**2
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    @validate_dimensions
    @convert_to_cm2
    def area(self):
        return self.length*self.width
    
class Triangle(Shape):
    def __init__(self,height,base):
        self.height=height
        self.base=base
    
    @validate_dimensions
    @convert_to_cm2
    def area(self):
        return 0.5*self.height*self.base
    
    
class Square(Shape):
    def __init__(self,length):
        self.length=length
    
    @validate_dimensions
    @convert_to_cm2
    def area(self):
        return self.length**2
    
    
class Rhombus(Shape):
    def __init__(self,length1,length2):
        self.length1=length1
        self.length2=length2
    
    @validate_dimensions
    @convert_to_cm2
    def area(self):
        return 0.5*self.length1*self.length2
    
     
class Trapezium(Shape):
    def __init__(self,length1,length2):
        self.length1=self.length1
        self.length2=length2
    
    @validate_dimensions
    @convert_to_cm2
    def area(self):
        return 0.5*self.length1*self.length2
    
    
def main():
    while True:
        print("\nWelcome to shape area calculator")
        print("1.Circle")
        print("2.Rectangle")
        print("3.Triangle")
        print("4.Square")
        print("5.Rhombus")
        print("6.Trapezium")
        print("7.Exit")
        
        
        choice=input("Enter your choice:")
        if choice=="1":
            radius=int(input("Enter the radius:"))
            shape=Circle(radius)
            print(f"The area is {shape.area()}")
        elif choice=="2":
            length=int(input("Enter the length:"))
            width=int(input("Enter the width:"))
            shape=Rectangle(length,width)
            print(f"The area is {shape}")
        elif choice=="3":
            height=int(input("Enter the heigth:"))
            base=int(input("Enter the base:"))
            shape=Triangle(height,base)
            print(f"The area is {shape.area()}")
        elif choice=="4":
            length=int(input("Enter the length:"))
            shape=Square(length)
            print(f"The area is {shape}")
        elif choice=="5":
            length=int(input("Enter the length:"))
            width=int(input("Enter the width:"))
            shape=Rhombus(length,width)
            print(f"The area is {shape.area()}")
        elif choice=="6":
            length=int(input("Enter the length:"))
            width=int(input("Enter the width:"))
            shape=Trapezium(length,width)
            print(f"The area is {shape.area()}")
        elif choice=="7":
            print("Goodbye!")
            break
        else:
            raise ValueError("Invalid choice")
            
            
if __name__=="__main__":
    main()     
                
                