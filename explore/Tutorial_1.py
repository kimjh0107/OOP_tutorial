class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

"""
Instance variables = variable which is declared in a class but ouside of constructors
"""
emp_1.first = 'Jong'
emp_1.last = 'Kim'
emp_1.email = 'sds@gmail.com'
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "Test.User@company.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

"""
Don't have to manually set all variables every time 
By creating init method, you can use as initialize, or construct when we create methods within a class they recevie the instacne 
as the first argument automatically 
"""

# %% 
class Employee:
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'

# init methods run automatically 
emp_1 = Employee('Jong', 'Kim', 3000)
emp_2 = Employee('Test', 'User', 2000)

print(emp_1.last)
print(emp_2.fullname) # function 이기에 fullname() 이런식으로 해야지 결과 출력 
print(emp_2.fullname()) # Test User

# %%
