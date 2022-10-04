# For Loop Review 

# range(start , end , step)

# for i in range(1, 11):  # A sequence from 1 to 10
#     if i % 2 == 0:
#         print(i, " is even")
#     else:
#         print(i, " is odd")


print('Example of range(start , end , step) without step')

for val in range(1,11):
    print(f'val = {val}')


print('\nExample of range(start , end , step) with step ')


for val in range(1,11,2):
    print(f'val = {val}')



print('Looping Through a List/String')

text = 'A list or string can be iterated through its indices.'

for val in text:
    print(f'val = {val}')

print('Looping Through a List/String with enumerated - this give the idx and value')
for idx,val in enumerate(text):
    print(f'idx = {idx},val = {val}')


print('Print of a Nested for loop')
n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]
found = False  # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if(n1 != n2):
            if(n1 + n2 == n):
                found = True  # Set found to True
                break  # Break inner loop if a pair is found
    if found:
        print(n1, n2) # Print the pair
        break  # Break outer loop if a pair is found

print(max(num_list))