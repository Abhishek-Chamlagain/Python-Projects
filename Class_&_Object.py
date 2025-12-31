"""To map with real world scenarios, we start using object in code. 
This is also called object oriented programming."""

'Class is a blueprint for creating object'

'Creating class'
# class Student:
#     name = "Abhishek Chamlagain"

'Creating object'
# S1 = Student()
# print(S1.name)

'Another Example'
# class Car:
#     color = "Black"
#     brand = "BMW"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

"Constructor"
'''All classes have a function called __init__(), 
which is always executed when the object is being initiated.'''

"Creating class"
# class Student:
#     def __init__(Self, name, Marks):
#         Self.name = name
#         Self.Marks=Marks
#         print("Adding new student in database....")

"Creating Object"
# S1=Student("Abhishek Chamlagain", 90)
# print(S1.name, S1.Marks)

# S2=Student("Rajiv Yadav",95)
# print(S2.name, S2.Marks)

"""NOTE: The self parameter is a refrence to the current instance of the class,
 and is used to access variable that belongs to the class"""

"""Types of Constructor"""

"""1. Default Constructor (With no parameter)"""
"""2. Parameterized Constructor (With Parameter)"""

# class Student:

#     def __init__(Self):  # Default Constructor
#         pass

#     def __init__(Self, name, Marks):  # Parameterized Constructor
#         Self.name = name
#         Self.Marks=Marks
#         print("Adding new student in database....")


# S1=Student("Abhishek Chamlagain", 90)
# print(S1.name, S1.Marks)

# S2=Student("Rajiv Yadav",95)
# print(S2.name, S2.Marks)


"""Class and Instance attribute"""

# class Student:
#      college = "Padmashree College"  # Class Attribute
#      name = "Shree"  # Class Attribute  (Here Object attribute > Class Attribute)

#      def __init__(Self, name, Marks):
#          Self.name = name   # Object attribute
#          Self.Marks=Marks
#          print("Adding new student in database....")


# S1=Student("Abhishek Chamlagain", 90)
# print(S1.name, S1.Marks)

# S2=Student("Rajiv Yadav",95)
# print(S2.name, S2.Marks)

# print(Student.college)
# print(S1.college)
# print(S2.college)

"""Note: Object attribute > Class attribute (Which is given in above example)"""


"""Methods"""
"""Methods are function that belong to objects"""

# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks

#     def display(self):
#         print("Hello",self.name)

#     def get_Marks(self):
#         return self.marks

# S1=Student("Abhishek", 89)
# print(S1.name, S1.marks)
# print(S1.get_Marks())

"""Practice question"""

"""Create student class that takes name and marks of 3 students as argument in constructor.
 Then create a method to print the average"""

# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks

#     def get_Average(self):
#         sum = 0
#         for val in self.marks:
#             sum+=val
#         print("Student Name: ", self.name, "\nAverage marks: ", sum/3)

# S1=Student("Abhishek Chamlagain", [80, 90, 78])
# S1.get_Average()

# """To change attriv=bute value"""
# S1.name="Ironman"
# S1.get_Average()

"""Static Methods"""
"""Methods that don't use the self parameter( Work at class level)"""
# class student:
#     @ staticmethod  #Decorator
#     def college():
#         print("Padmashree College")

# S1=student()
# S1.college()

"""Decorators allows us to wrap another function in order to extend the 
behaviour of the wrapped function, without permanently modifying it"""

"""Important Topic"""

"""Abstraction
 Hiding the implementation details of a class and only showing the essential features to the user"""

"""Encapsulation
Wrapping data and functions into a single unit (Object)"""

"""Practice Question
Create Account class with 2 attribute- Balance and account_no.
create methods for debit, credit & printing the balance"""

# class Account:

#     def __init__(self, balance, account_no):
#         self.balance=balance
#         self.account_no=account_no

#     def debit(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance-=amount
#             print("Rs.", amount,"was debitted")
#             print("In account: ",self.account_no," available amount is = ", self.get_balance())

#     def credit(self, amount):
#         self.balance+=amount
#         print("Rs.",amount,"was creditted")
#         print("In account: ",self.account_no," available amount is = ", self.get_balance())

#     def get_balance(self):
#         return self.balance

# Acc1=Account(100000, 4941)

# while True:

#     print("\nWelcome to Bank")

#     print("Enter 1 to Deposit cash \nEnter 2 to withdraw cash\nEnter 3 to exit")
#     Num=int(input("Input: "))

#     if Num==1:
#         cre=int(input("Enter amount to deposit: "))
#         Acc1.credit(cre)
#         choice = input("Do you want to continue? (y/n): ")
#         if choice.lower() != 'y':
#             break

#     elif Num==2:
#         deb=int(input("Enter amount to withdraw: "))
#         Acc1.debit(deb)
#         choice = input("Do you want to continue? (y/n): ")
#         if choice.lower() != 'y':
#             break

#     elif Num==3:
#         print("\nThank you for banking with us...\nPlease visit again\n")
#         break
    
#     else:
#         print("Enter valid input.... Please try again\n")

"""del Keyword
It is used to delete object properties or object itself"""

# class Student:
#     def __init__(self, name):
#         self.name=name
        
# s1=Student("Abhishek")
# print(s1.name)
# del s1.name
# print(s1.name)


"""Private (like) attributes and methods

Conceptual inheritance in Pytho 
Private attribute and methods are meant to be used only 
within the class and are not assible from outside the class"""

"""To make private we use '__' symbol before attribute or methods"""

# class Person:
#     __name="Abhishek"

#     def __hello(self):
#         print("Hello ", self.__name)
    
#     def welcome(self):
#         self.__hello()

# P1=Person()
# P1.welcome()

"""Inheritance
When one class (child/derived) derives the properties and method of another class (Parent/base)"""

"""Example"""
# class Car:
#     color="Black"

#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name=name

# car1=ToyotaCar("Fortuner")
# car2=ToyotaCar("Prius")

# print(car1.name)
# car1.start()
# print(car1.color)

"""Types of inheritance

1. Single inheritance (One child class derived from base calss ... same as example above)
   One parent → one child"""
# class Parent:
#     def show(self):
#         print("This is Parent class")

# class Child(Parent):
#     def display(self):
#         print("This is Child class")

# obj = Child()
# obj.show()
# obj.display()


"""2. Multilevel inheritance (Grandparent → Parent → Child)"""
# class GrandParent:
#     def gp_method(self):
#         print("Grand Parent class")

# class Parent(GrandParent):
#     def p_method(self):
#         print("Parent class")

# class Child(Parent):
#     def c_method(self):
#         print("Child class")

# obj = Child()
# obj.gp_method()
# obj.p_method()
# obj.c_method()


""" Multiple Inheritance (One child → multiple parents)"""

# class Father:
#     def father_method(self):
#         print("Father class")

# class Mother:
#     def mother_method(self):
#         print("Mother class")

# class Child(Father, Mother):
#     def child_method(self):
#         print("Child class")

# obj = Child()
# obj.father_method()
# obj.mother_method()
# obj.child_method()

"""Super method()
Super() method is used to access methods of the parent class"""

# class car:
#     def __init__(self, type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("Engine start")

#     @staticmethod
#     def end():
#         print("Engine stop")

# class ToyotaCar(car):
#     def __init__(self,name, type):
#         super().__init__(type)
#         self.name=name
#         super().start()

# car1=ToyotaCar("Fortuner","Petrol")
# print(car1.name)

"""Class method
A class method is bound to the class and receives the class as an implicit first argument.
Note: Static method can't access or modify class state and generally for unity"""

# class Person:
#     name = "anonymus"

#     """def changeName(self, name):
#         # Person.name = name  #First way
#         self.__class__.name ="Abhishek Chamlagain"  # Second Way
#         """
# # But here we use class method to access it

#     @classmethod
#     def changeName(cls, name):
#         cls.name=name
        
# p1=Person()
# p1.changeName("Abhishek")
# print(p1.name)
# print(Person.name)

"""Note: Methods type
static method
class method (Cls)
instance method (self)"""

"""Property Decorator
We use @property decorator on any method in 
the class to use the method as a property"""

# class student:
#     def __init__(self, phy, chem, math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math

#     @property
#     def percentage(self):
#         return str(( self.phy + self.chem + self.math)/3)+"%"
    
# stu1=student(90, 95, 90)
# print(stu1.percentage)

# stu1.phy=76
# print(stu1.percentage)


"""Polymorphism: Operator overloading
When the same poerator is allowed to have different meaning according to the context"""

"""Dealing with complex number"""

# class Number:
#     def __init__(self, real, img):
#         self.real=real
#         self.img=img

#     def shownumber(self):
#         print(self.real,"i + ",self.img,"j")

#     def add(self, num2):
#         newReal= self.real + num2.real
#         newImg= self.img + num2.img
#         return Number(newReal, newImg)

# Num1=Number(5,8)
# Num1.shownumber()

# Num2=Number(9,6)
# Num2.shownumber()

# num3=Num1.add(Num2)
# num3.shownumber()


''' Now solving problem using DUNDER Function'''
# class Number:
#     def __init__(self, real, img):
#         self.real=real
#         self.img=img

#     def shownumber(self):
#         print(self.real,"i + ",self.img,"j")

#     def __add__(self, num2):
#         newReal= self.real + num2.real
#         newImg= self.img + num2.img
#         return Number(newReal, newImg)
    
#     def __sub__(self, num2):
#         newReal= self.real - num2.real
#         newImg= self.img - num2.img
#         return Number(newReal, newImg)

# Num1=Number(5,8)
# Num1.shownumber()

# Num2=Number(9,6)
# Num2.shownumber()

# # num3=Num1 + Num2  #For aaddition
# num3=Num1 - Num2  # For subtraction
# num3.shownumber()


"""Practice Question"""

"""1. Define a circle class to create a circle with radious r using the constructor. 
      Define a Area() method of the class which calculates the area of the circle.
      Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle"""

# class Circle:
#     def __init__(self,radious):
#         self.r=radious

#     def Area(self):
#        return (22/7)*self.r**2
    
#     def Perimeter(self):
#         return 2*(22/7)*self.r
    
# inp=float(input("Enter radious of circle to find its 'Area' and 'Perimeter': "))
# C1=Circle(inp)
# print(C1.Area())
# print(C1.Perimeter())

"""2. Define a Employee class with attributes role, department, and salary. 
      This class also has a showDetails()method. Create an Engineer class that inherits properties from 
      Employee and has additional attributes: name & age"""

# class Employee:
#     def __init__(self, role, department, salary):
#         self.role=role
#         self.department=department
#         self.salary=salary

#     def showDetails(self):
#         print("Role= ",self.role)
#         print("Department= ",self.department)
#         print("Salary= ",self.salary)
    
# class Engineer(Employee):
#     def __init__(self, name, age):
#          self.name=name
#          self.age=age
#          super().__init__("Project Manager", "IT", "100000")
#          super().showDetails()

# print("Enter 'Name' and 'Age' to find person role, department, salary")
# inp=input("Enter name: ")
# Ag=int(input("Enter Age: "))
# Eng1=Engineer(inp, Ag)
    
"""Create a class called order which stores items and its price. Under dunder function __gt__() 
to convey that Order1>Order2 if price of Order1>price of Order 2"""

# class Order:
#     def __init__(self, items, price):
#         self.items=items
#         self.price=price

#     def __gt__(self, order2):
#        return self.price>order2.price

# order1=Order("Bugati",20)
# order2=Order("Farari",15)
# print(order1>order2)