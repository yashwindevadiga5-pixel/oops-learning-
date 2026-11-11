# abstraction
from abc import ABC,abstractclassmethod
from math import pi

class shape:
    abstractclassmethod
    def __init__(self):
        self.area=0

    abstractclassmethod
    def take_input(self):
        pass

    abstractclassmethod
    def calculate_area(self):
        pass

    abstractclassmethod
    def display(self):
        pass


class square(shape):
    def __init__(self):
        self.side=0
        self.area=0

    def take_input(self):
        self.side=int(input("enter side"))

    def calculate_area(self):
        self.area=self.side*self.side

    def display(self):
        print(f"area of square {self.area}")

class circle:
    def __inint__(self):
        self.radius=0

    def take_input(self):
        self.radius=int(input("enter radius"))

    def calculate_area(self):
        self.area=pi*self.radius**2

    def display(self):
        print(f"area of circle {self.area}")
      
class rectangl:
    def __init__(self):
        self.lenth=0
        self.width=0

    def take_input(self):
        self.lenth=int(input("enter the lenth"))
        self.width=int(input("enter the width"))

    def calculate_area(self):
        self.area=(self.lenth*self.width)

    def display(self):
        print(f"area of rectangle is{self.area}")

def main():
    print("1.square\n2.circle\n3.rectangl\n")
    choice =int(input("enter a choice"))
    if choice==1:
        p=square()
    elif choice==2:
        p=circle()
    elif choice==3:
        p=rectangl()
   
    p.take_input()
    p.calculate_area()
    p.display()

if __name__=='__main__':
    main()