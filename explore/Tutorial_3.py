class Employee:

  num_of_emps = 0
  raise_amount = 1.04 

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last 
    self.pay = pay 
    self.email = first + "." + last + "@company.com"

    Employee.num_of_emps += 1
  
  def fullname(self):
    return f"{self.first} {self.last}"

  def apply_raise(self):
    self.pay = int(self.pay * raise_amount)

  @classmethod # classmethod를 통해서 classmethod를 지정 가능 
  def set_raise_amt(cls, amount):
    cls.raise_amt = amount        

# new classmethod 
  @classmethod 
  def from_string(cls,emp_str):
      first, last, pay = emp_str.split("-")
      return cls(first, last, pay)

  @staticmethod 
  def is_workday(day):
      if day.weekday() == 5 or day.weekday() == 6:
          return False 
      return True 


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
# class method안에 전부 들어갔다 나오는 구조로 역할을 하기 때문에 classmethod가 값이 변경되는 것을 확인 가능 


emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.first)
print(new_emp_1.email)
print(new_emp_1.pay)

import datetime 
my_date = datetime.date(2016,7,10)

print(Employee.is_workday(my_date))