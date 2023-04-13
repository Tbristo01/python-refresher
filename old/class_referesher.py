# Format of A Class
class MyClass:
    pass


obj = MyClass()  # creating a MyClass Object
print(obj)

# How to access the property of a class 

# creating a calls with variables not assigned with any details
# this code will compile
class Employee:
    # defining the properties and assigning them none
    ID = None
    salary = None
    department = None


Tishaun = Employee()


print(Tishaun)

Tishaun.ID="123435"
Tishaun.salary="$132456789"
Tishaun.department ="Engineering"


# cerating an object of the Employee class
# Printing properties of Tishaun
print("ID =", Tishaun.ID)
print("Salary", Tishaun.salary)
print("Department:", Tishaun.department)


Tishaun.title = "Manager"



print("ID =", Tishaun.ID)
print("Salary", Tishaun.salary)
print("Department:", Tishaun.department)
print("Title:", Tishaun.title)




class Employee:
    # defining the properties and assigning them None
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)



class Employee:
    # defining the properties and assigning None to them
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee()
Mark = Employee("3789", 2500, "Human Resources")

# Printing properties of Steve and Mark
print("Steve")
print("ID :", Steve.ID)
print("Salary :", Steve.salary)
print("Department :", Steve.department)
print("Mark")
print("ID :", Mark.ID)
print("Salary :", Mark.salary)
print("Department :", Mark.department)



nums = [4, 1, 3, 2]
rev = reversed(nums)

print(rev)


print(sorted(rev) == sorted(rev))



# Initializer with optional parameters

class Student:
    # defining the properties and assigning None to them
    def __init__(self,name=str,id=str,ranking=int,grade_level=str) -> None:
        self.name=name
        self.id=id
        self.ranking=ranking
        self.grade_leve=grade_level

# creating an object of the Student class with default parameters
print('Default Values')
Tishaun =Student()
print(f'name: {Tishaun.name}')
print(f'id: {Tishaun.id}')
print(f'ranking:{Tishaun.ranking}')
print(f'grade_level{Tishaun.grade_leve}')

print('Values after assignment to objest properties')
Tishaun= Student('Tishaun Bristol','gihkjlhgkjbhkj',1,'Senior')
print(f'name: {Tishaun.name}')
print(f'id: {Tishaun.id}')
print(f'ranking:{Tishaun.ranking}')
print(f'grade_level{Tishaun.grade_leve}')

