project : 0x0A. Python - Inheritance

A language feature would not be worthy of the name “class” without supporting inheritance. The syntax for a derived class definition looks like this:

class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
The name BaseClassName must be defined in a namespace accessible from the scope containing the derived class definition. In place of a base class name, other arbitrary expressions are also allowed

Inheritance in Python :
One of the core concepts in object-oriented programming (OOP) languages is inheritance. It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class.

Mandatory tasks :
0. Lookup
Write a function that returns the list of available attributes and methods of an object
1. My list
Write a class MyList that inherits from list
2. Exact same object
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False
3. Same class or inherit from
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
4. Only sub class of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
5. Geometry module
Write an empty class BaseGeometry.
6. Improve Geometry
Write a class BaseGeometry (based on 5-base_geometry.py).
7. Integer validator
Write a class BaseGeometry (based on 6-base_geometry.py).
8. Rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
9. Full rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
10. Square #1
Write a class Square that inherits from Rectangle (9-rectangle.py)
11. Square #2
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

Advanced tasks :
12. My integer
Write a class MyInt that inherits from int:
MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module
13. Can I?
Write a function that adds a new attribute to an object if it’s possible:
Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
You are not allowed to use try/except
You are not allowed to import any module
