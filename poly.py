# Method Overriding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()


# Duck Typing
# class Python:
#     def execute(self):
#         print("Python is executing")

# class Java:
#     def execute(self):
#         print("Java is executing")

# def run(obj):
#     obj.execute()

# p = Python()
# j = Java()

# run(p)
# run(j)