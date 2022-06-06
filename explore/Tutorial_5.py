class Employee:

  raise_amount = 1.04 

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = f'{first}.{last}@company.com'

  def fullname(self):
    return f'{self.first} {self.last}'
  
  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

  # return a string that can use to recreate the object 
  def __repr__(self):
    return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
  
  def __str__(self):
    return f'{self.fullname()} - {self.email}'

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())


# %% 
# Dunder method - special method, dunder add method 
print(1*2)
print(int.__add__(1,2)) # 3
print(str.__add__('a','b')) # ab


# %%
class Employee:

  raise_amount = 1.04 

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = f'{first}.{last}@company.com'

  def fullname(self):
    return f'{self.first} {self.last}'
  
  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

  # return a string that can use to recreate the object 
  def __repr__(self):
    return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
  
  def __str__(self):
    return f'{self.fullname()} - {self.email}'

  def __add__(self, other):
      return self.pay + other.pay
  
  def __len__(self):
      return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)
print(emp_1 + emp_2)  # 이 부분은 __add__ 함수를 만들어주었기 때문에 실행 가능 

print(len("test"))
print('test'.__len__())
