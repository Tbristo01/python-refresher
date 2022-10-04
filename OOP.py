# class Employee:
#     # defining the properties and assigning values to them
#     ID = None
#     salary = None
#     department = None


# # cerating an object of the Employee class
# Steve = Employee()


# # assigning values to properties of Steve - an object of the Employee class
# Steve.ID = 3789
# Steve.salary = 2500
# Steve.department = "Human Resources"

# # printing properties of Steve - an object of the Employee class
# print("ID =", Steve.ID)
# print("Salary:$", Steve.salary)
# print("Department:$", Steve.salary)


# # creating a new attribute for Steve
# Steve.title = "Manager"

# print("ID =", Steve.ID)
# print("Salary:$", Steve.salary)
# print("Department:", Steve.salary)
# print("Title:", Steve.title)


# class Employee:
#     # defining the properties and assigning them None
#     def __init__(self, ID, salary, department):
#         self.ID = ID
#         self.salary = salary
#         self.department = department


# # creating an object of the Employee class with default parameters
# Steve = Employee(3789, 2500, "Human Resources")

# # Printing properties of Steve
# print("ID :", Steve.ID)
# print("Salary :", Steve.salary)
# print("Department :", Steve.department)


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