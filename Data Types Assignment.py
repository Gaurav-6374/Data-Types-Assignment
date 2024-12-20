# Data Types Assignment

#1. What are data structures, and why are they important?
'''Data structures are organized ways to store, manage, and retrieve data efficiently. They are essential for optimizing 
performance in data manipulation, storage, and algorithm design.'''

#2. Explain the difference between mutable and immutable data types with examples.
'''Mutable: Can be changed after creation (e.g., lists: a = [1, 2], a[0] = 3).
Immutable: Cannot be changed after creation (e.g., tuples: a = (1, 2); elements can't be reassigned).'''
                                             
#3. What are the main differences between lists and tuples in Python?
'''Lists: Mutable, slower, can grow or shrink.
Tuples: Immutable, faster, fixed size.'''

#4. Describe how dictionaries store data.
'''Dictionaries store data as key-value pairs using a hash table for quick access.'''

#5. Why might you use a set instead of a list in Python?
'''Sets automatically remove duplicate values and support fast membership testing.'''

#6. What is a string in Python, and how is it different from a list?
'''A string is an immutable sequence of characters, whereas a list is a mutable sequence of any data type.'''

#7. How do tuples ensure data integrity in Python?
'''Tuples are immutable, ensuring data cannot be accidentally modified, making them ideal for fixed data.'''

#8. What is a hash table, and how does it relate to dictionaries in Python?
'''A hash table maps keys to values using a hashing function. Python dictionaries are implemented as hash tables for fast 
key-based lookups.'''

#9. Can lists contain different data types in Python?
'''Yes, lists can hold mixed data types (e.g., [1, "text", 3.5]).'''

#10. Explain why strings are immutable in Python.
'''Strings are immutable to optimize performance, ensure hashability, and prevent accidental modifications.'''

#11. What advantages do dictionaries offer over lists for certain tasks?
'''Dictionaries allow fast access to values using keys, making them ideal for tasks requiring key-based lookups.'''

#12. Describe a scenario where using a tuple would be preferable over a list.
'''Use tuples for fixed collections like coordinates (x, y) or constant configuration values.'''

#13. How do sets handle duplicate values in Python?
'''Sets automatically remove duplicate values, ensuring each element is unique.'''

#14. How does the “in” keyword work differently for lists and dictionaries?
'''Lists: Checks if the value exists.
Dictionaries: Checks if the key exists.'''

#15. Can you modify the elements of a tuple? Explain why or why not.
'''No, tuples are immutable, so their elements cannot be modified after creation.'''

#16. What is a nested dictionary, and give an example of its use case.
'''A nested dictionary contains dictionaries as values. Example: { "student1": {"name": "John", "age": 20} }, used for hierarchical data.'''

#17. Describe the time complexity of accessing elements in a dictionary.
'''Accessing elements in a dictionary has an average time complexity of O(1) due to hashing.'''

#18. In what situations are lists preferred over dictionaries?
'''Lists are preferred when maintaining order or working with sequential data.'''

#19. Why are dictionaries considered unordered, and how does that affect data retrieval?
'''Dictionaries prior to Python 3.7 are unordered, meaning key-value pairs are not stored in a predictable order, 
but retrieval is still efficient by key.'''

#20. Explain the difference between a list and a dictionary in terms of data retrieval.
'''List: Access elements by index.
Dictionary: Access elements by key.'''


#11. Create a string with your name and print it
 '''
name = "Gaurav"
print(name)'''

#12. Find the length of the string "Hello World"
'''string = "Hello World"
print(len(string))'''

#13. Slice the first 3 characters from the string "Python Programming"
'''
string = "Python Programming"
print(string[:3])'''

#14. Convert the string "hello" to uppercase
'''
string = "hello"
print(string.upper())'''

#15. Replace the word "apple" with "orange" in the string "I like apple"
'''
string = "I like apple"
print(string.replace("apple", "orange"))'''

#16. Create a list with numbers 1 to 5 and print it
'''
numbers = [1, 2, 3, 4, 5]
print(numbers)'''

#17. Append the number 10 to the list [1, 2, 3, 4]
'''
numbers = [1, 2, 3, 4]
numbers.append(10)
print(numbers)'''

#18. Remove the number 3 from the list [1, 2, 3, 4, 5]
'''
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)'''

#19. Access the second element in the list ['a', 'b', 'c', 'd']
'''
letters = ['a', 'b', 'c', 'd']
print(letters[1])'''

#20. Reverse the list [10, 20, 30, 40, 50]
'''
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)'''



#21. Create a tuple with the elements 10, 20, 30 and print it
'''
tuple1 = (10, 20, 30)
print(tuple1)'''

#22. Access the first element of the tuple ('apple', 'banana', 'cherry')
'''
tuple2 = ('apple', 'banana', 'cherry')
print(tuple2[0])'''

#23. Count how many times the number 2 appears in the tuple (1, 2, 3, 2, 4, 2)
'''
tuple3 = (1, 2, 3, 2, 4, 2)
print(tuple3.count(2))'''

#24. Find the index of the element "cat" in the tuple ('dog', 'cat', 'rabbit')
'''
tuple4 = ('dog', 'cat', 'rabbit')
print(tuple4.index('cat'))'''

#25. Check if the element "banana" is in the tuple ('apple', 'orange', 'banana')
'''
tuple5 = ('apple', 'orange', 'banana')
print('banana' in tuple5)'''

#26. Create a set with the elements 1, 2, 3, 4, 5 and print it
'''
set1 = {1, 2, 3, 4, 5}
print(set1)'''

#27. Add the element 6 to the set {1, 2, 3, 4}

'''
set2 = {1, 2, 3, 4}
set2.add(6)
print(set2)'''


#28. Create a tuple with the elements 10, 20, 30 and print it
'''
tuple1 = (10, 20, 30)
print(tuple1)'''

#29. Access the first element of the tuple ('apple', 'banana', 'cherry')
'''
tuple2 = ('apple', 'banana', 'cherry')
print(tuple2[0])'''

#30. Count how many times the number 2 appears in the tuple (1, 2, 3, 2, 4, 2)
'''
tuple3 = (1, 2, 3, 2, 4, 2)
print(tuple3.count(2))'''

#31. Find the index of the element "cat" in the tuple ('dog', 'cat', 'rabbit')
'''
tuple4 = ('dog', 'cat', 'rabbit')
print(tuple4.index('cat'))'''


#32. Check if the element "banana" is in the tuple ('apple', 'orange', 'banana')
'''
tuple5 = ('apple', 'orange', 'banana')
print('banana' in tuple5)'''

#33. Create a set with the elements 1, 2, 3, 4, 5 and print it
'''
set1 = {1, 2, 3, 4, 5}
print(set1)'''

#34. Add the element 6 to the set {1, 2, 3, 4}
'''
set2 = {1, 2, 3, 4}
set2.add(6)
print(set2)'''












