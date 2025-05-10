#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📝 OOP Practice Homework - Task 3: More Inheritance Practice
Date: May 8, 2025

======================================================================
📌 Task 3: More Inheritance Practice
======================================================================
Create another subclass called Teacher that inherits from Person:
- Add an instance variable subject (str)
- Add a method teach() that prints "Teacher {name} is teaching {subject}."
- Override the __str__ method to return "Teacher(name=name, age=age, subject=subject)"
"""
class Teacher:
  def __init__(self,name,age,subject):
    self.name=name
    self.age=age
    self.subject=subject
  def teach(self):
    return f"Teacher{self.name} is teaching {self.subject}"
  def __str__(self):
    return f"Teacher{self.name,self.age,self.subject}"
asd=Teacher("Samiya",34,"OOP")
print(asd.teach())
print(asd.__str__())
