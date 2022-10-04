# Order of Growth	Name
# O(1)	constant
# O(logb n)	logarithmic (for any b)
# O(n)	linear
# O(n logb n)	“en log en”
# O(n2)	quadratic
# O(n3)	cubic
# O(cn)	exponential (for any c)
# O(n!) Factorial 



from array import array


print("Big O(1) =	constant")
print("Example:")
print("""

def constant_function(array):
    retunr(1000*1000000) -> O(1)
""")

arr=['1...20']
def constant_function(arr):
    return(1000*1000000)

print(constant_function(arr))




print('Big O(n) = Linear')
print('Example:')
print(
'''
def linear_function(arr):
    for i in range(len(arr)): -> O(n)
        print(1000 * 10000) -> O(1)
        something = (20000000 * 200) / 2 -> O(1)
        print(something) -> O(1)

'''
)


def linear_function(arr):
    for i in range(len(arr)):
        print(1000 * 10000)
        something = (20000000 * 200) / 2
        print(something)

linear_function(arr=arr)




def square(n):
    for i in range(0,n):
        for j in range(0,n):
            print(i,j)


square(4)