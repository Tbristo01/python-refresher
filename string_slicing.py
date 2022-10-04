slicing ="Slicing is the process of obtaining a portion (substring) of a string by using its indices."

print(slicing.title())
print("string[start:end]")

my_string = "This is MY string!"
print(my_string[0:4]) # From the start till before the 4th index
print(my_string[1:7])
print(my_string[8:len(my_string)]) # From the 8th index till the end
print("\n")

print("string[start:end:step]")
my_string = "This is MY string!"
print(my_string[0:7])  # A step of 1
print(my_string[0:7:2])  # A step of 2
print(my_string[0:7:5])  # A step of 5

print("\n")
print("Reverse Slicing")
print("Strings can also be sliced to return a reversed substring. In this case, we would need to switch the order of the start and end indices.")
my_string = "This is MY string!"
print(f"\nOriginal String: {my_string}")
print(my_string[13:2:-1]) # Take 1 step back each time
print(my_string[17:0:-2]) # Take 2 steps back. The opposite of what happens in the slide above



print("\nPartial Slicing")
my_string = "This is MY string!"
print(f"Original String: {my_string}")
print(my_string[:8])  # All the characters before 'M'
print(my_string[8:])  # All the characters starting from 'M'
print(my_string[:])  # The whole string
print(my_string[::-1])  # The whole string in reverse (step is -1)