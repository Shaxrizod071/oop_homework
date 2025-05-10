#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📝 OOP Practice Homework - Bonus Task: Polymorphism
Date: May 8, 2025

======================================================================
🎯 Bonus Task (Optional): Polymorphism
======================================================================
Write a function called introduce_people(people_list) that loops through a list of Person objects
(can be Person, Student, or Teacher) and calls their greet() method. Demonstrate how different
objects behave differently even though the method name is the same.
"""
class Person:
   def __init__(self,name,age) :
        self.name=name
        self.age=age
class Stusent(Person):
    def greet(self,name,age):
        self.neme=name
        self.age=age
class Teacher(Person):
     def greet(self,name,age):
        self.name=name
        self.age=age
people_list=Teacher("Bahora",34)
print(people_list.name)
print(people_list.age)
  
    
