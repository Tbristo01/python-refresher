print("String".upper())
# A string is a collection of characters closed within single, double or triple quotation marks.

print("Harry Potter!")  # Double quotation marks

got = 'Game of Thrones...'  # Single quotation marks
print(got)
print("$")  # Single character

empty = ""
print(empty)  # Just prints an empty line

multiple_lines = '''Triple quotes allows
multi-line string.'''
print(multiple_lines)


print("The length of a string can be found using the len() function")
random_string = "I am Batman"  # 11 characters
print(f"For example : {random_string}")
print(f"length = {len(random_string)}")


# Indexing
#  string in Python is indexed from 0 to n-1 where n is its length. This means that the index of the first character in a string is 0.

batman = "Bruce Wayne"
print(f"string: {batman}")

first = batman[0]  # Accessing the first character

print(first)

space = batman[5]  # Accessing the empty space in the string
print(space)

last = batman[len(batman) - 1]
print(last)
# The following will produce an error since the index is out of bounds
# err = batman[len(batman)]


batman = "Bruce Wayne"
print(batman[-1])  # Corresponds to batman[10]
print(batman[-5])  # Corresponds to batman[6]