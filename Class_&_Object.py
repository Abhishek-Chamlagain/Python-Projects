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
class Student:
    def __init__(Self, name, Marks):
        Self.name = name
        Self.Marks=Marks
        print("Adding new student in database....")

"Creating Object"
S1=Student("Abhishek Chamlagain", 90)
print(S1.name, S1.Marks)

S2=Student("Rajiv Yadav",95)
print(S2.name, S2.Marks)

"""NOTE: The self parameter is a refrence to the current instance of the class,
 and is used to access variable that belongs to the class"""
