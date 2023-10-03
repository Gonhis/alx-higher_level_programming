project : 0x09. Python - Everything is object

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
OK. But what about this?

>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

All your answers should be only one line in a file. No space before or after the answer.

Mandatory tasks :

0. Who am I?
What function would you use to get the type of an object?
Write the name of the function in the file, without ().
1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without ().
2. Right count
In the following code, do a and b point to the same object? Answer with Yes or No.
3. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.
4. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.
5. Right count =+
In the following code, do a and b point to the same object? Answer with Yes or No.
6. Is equal
What do these 3 lines print?
7. Is the same
What do these 3 lines print?
8. Is really equal
What do these 3 lines print?
9. Is really the same
What do these 3 lines print?
10. And with a list, is it equal
What do these 3 lines print?
11. And with a list, is it the same
What do these 3 lines print?
12. And with a list, is it really equal
What do these 3 lines print?
13. And with a list, is it really the same
What do these 3 lines print?
14. List append
What does this script print?
15. List add
What does this script print?
16. Integer incrementation
What does this script print?
17. List incrementation
What does this script print?
18. List assignation
What does this script print?
19. Copy a list object
Write a function def copy_list(l): that returns a copy of a list.
20. Tuple or not?
a = ()
Is a a tuple? Answer with Yes or No.
21. Tuple or not?
a = (1, 2)
Is a a tuple? Answer with Yes or No.
22. Tuple or not?
a = (1)
Is a a tuple? Answer with Yes or No.
23. Tuple or not?
a = (1, )
Is a a tuple? Answer with Yes or No.
24. Who I am?
What does this script print?
25. Tuple or not
What does this script print?
26. Empty is not empty
What does this script print?
27. Still the same?
Will the last line of this script print 139926795932424? Answer with Yes or No.
28. Same or not?
Will the last line of this script print 139926795932424? Answer with Yes or No.

Advanced tasks :

29. #pythonic
Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code)
30. Low memory cost
Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
31. int 1/3
Assuming we are using a CPython implementation of Python3 with default options/configuration:
How many int objects are created by the execution of the first line of the script? (103-line1.txt)
How many int objects are created by the execution of the second line of the script (103-line2.txt)
32. int 2/3
Assuming we are using a CPython implementation of Python3 with default options/configuration
33. int 3/3
Assuming we are using a CPython implementation of Python3 with default options/configuration
34. Clear strings
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word).
