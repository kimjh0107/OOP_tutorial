"""
Instance variables가 사람의 이름과 같이 각각의 instance마다 가지고 있는 고유한 데이터라면, 
class variables는 한 단체의 단체명과 같은 class로 만들어진 모든 insatance가 공유하는 데이터라고 생각하면 됨 
"""

class Employee:

    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # self pay에 대해 새롭게 값을 지정해줬기에 값이 변경되어 나오는 것을 확인 가능 -> apply_raise()를 했을 경우


emp_1 = Employee('Jong', 'Kimg', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.pay) # 50000
# print(test2) ->  바로 이렇게 불러올 경우는 값이 변경 x 
emp_1.apply_raise()
print(emp_1.pay) # 52000
print(emp_1.__dict__) # pay가 변경된 것 확인 가능 
print(Employee.__dict__)

"""
여기서 확인 가능한 것은 : raise_amount같은 변수를 class variables라고 하는것 
전체 class 대상으로 한 변수이기에 각각의 instance variable들에 대해서는 결과가 나오지 않는 것을 확인 가능
"""

# class variables의 경우 외부에서 변경을 해줘도 값이 변경되는 것을 확인 가능 
print(Employee.raise_amount) # 1.04 
Employee.raise_amount = 1.05 
print(Employee.raise_amount) # 1.05 

# 이렇게 전체 class variables에 대해서 변경하면 값이 변경되지만 instance variable하나에 대해서만 변경하면 전체에 적용 x 
emp_1.raise_amount = 1.10 
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)



# %%
# 다른 example 
class Employee:

    num_of_emps = 0 # 새로운 class variables 
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1 
        
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   

# %%
print(Employee.num_of_emps)
emp_1 = Employee('Corey', 'Schafer', 50000)
print(Employee.num_of_emps)
emp_2 = Employee('Test', 'User', 60000)
print(Employee.num_of_emps)