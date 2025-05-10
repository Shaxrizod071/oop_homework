
"""
📝 OOP Practice Homework - Task 2: Inherit from the Base Class
Date: May 8, 2025

======================================================================
📌 Task 2: Inherit from the Base Class
======================================================================
Create a subclass called Student that inherits from Person:
- Add an instance variable grade (str)
- Add a method study() that prints "Student {name} is studying."
- Override the __str__ method to include the grade
  (e.g., "Student(name=name, age=age, grade=grade)")
"""
class Student:
  def __init__(self,name,age,grade):
     self.name=name
     self.age=age
     self.grade=grade
  def study(self):
    return (f"Hi {self.name} is studying")
  def __str__(self):
    return f"Hello {self.name} I am {self.age} years ago and I have got {self.grade}"
asd=Student("Samae",21,5)
print(asd.study())
print(asd.__str__())
