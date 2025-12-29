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

class Account:

    def __init__(self, balance, account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print("Rs.", amount,"was debitted")
            print("In account: ",self.account_no," available amount is = ", self.get_balance())

    def credit(self, amount):
        self.balance+=amount
        print("Rs.",amount,"was creditted")
        print("In account: ",self.account_no," available amount is = ", self.get_balance())

    def get_balance(self):
        return self.balance

Acc1=Account(100000, 4941)

while True:

    print("\nWelcome to Bank")

    print("Enter 1 to Deposit cash \nEnter 2 to withdraw cash\nEnter 3 to exit")
    Num=int(input("Input: "))

    if Num==1:
        cre=int(input("Enter amount to deposit: "))
        Acc1.credit(cre)
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

    elif Num==2:
        deb=int(input("Enter amount to withdraw: "))
        Acc1.debit(deb)
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

    elif Num==3:
        print("\nThank you for banking with us...\nPlease visit again\n")
        break
    
    else:
        print("Enter valid input.... Please try again\n")
        









