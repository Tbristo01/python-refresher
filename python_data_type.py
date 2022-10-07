'''
Immutable is the when no change is possible over time. 
In Python, if the value of an object cannot be changed over time, then it is known as immutable. 
Once created, the value of these objects is permanent.

Immutable Data Type 
1.Number - int , float , complex
2.String - str
3.Tuple 
'''

# 1.Number - int , float , complex
x = 1
print(f'type of {x} : {type(x)}')

x = 12.5
print(f'type of {x} : {type(x)}')

x = 10 + 20j
print(f'type of {x} : {type(x)}')

print('\n')

# 2.String - str
str1='This is a string in Python' 
print(f'type of {str1}: {type(str1)}')
print('\n')

# 3.Tuple 
names = ('Jeff', 'Bill', 'Steve', 'Yash') # string tuple
print(names)
print(f'type of {names}: {type(names)}')
print(names[0])

print('\n')

'''
Booleans represent one of two values: True or False.
The bool() function allows you to evaluate any value, and give you True or False in return.
'''
x = True  # 1
y = False # 0


print(f'type of {x}: {type(x)}')
print(f'type of {y}: {type(y)}')
print('\n')

'''
Mutable is when something is changeable or has the ability to change. 
In Python, 'mutable' is the ability of objects to change their values. 
These are often the objects that store a collection of data.
'''

'''
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets:
'''

thislist = ["apple", "banana", "cherry"]
print(f'type of {thislist}: {type(thislist)}')
print(thislist[0])
thislist[0]='Lychee'
print(thislist,end="\n\n")

'''
Dictionary Items
Dictionary items are ordered, changeable, and does not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f'type of {thisdict}: {type(thisdict)}')

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(f'type of {my_set}: {type(my_set)}')

'''
Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items.
'''

thisset = {"apple", "banana", "cherry", "apple"}
print(f'type of {thisset}: {type(thisset)}')