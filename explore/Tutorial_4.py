# %% 
class Employee:

  raise_amount = 1.04 

  def __init__(self, first, last, pay):
    self.frist = first
    self.last = last 
    self.pay = pay 
    self.email = first + '.' + last + '@company.com'

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)


class Developer(Employee): # Employee class를 inherit 
    pass 

# Employee가 아닌 Developer로 불러와도 동일하게 진행 -> 왜냐하면 employee class를 inherit 받았기 때문 
dev_1 = Developer('Jay', 'Kim', 50000)
dev_2 = Developer('Test', 'Employee', 60000)

# 안에 function들 또한 동일하게 적용 가능 
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)



# %% 
# Class Developer 추가 
class Employee:

  raise_amount = 1.04 

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last 
    self.pay = pay 
    self.email = first + '.' + last + '@company.com'

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
    # 추가적으로 위에 상속받은 함수들에 대해서 추가적으로 기능 더 추가 가능 
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        """위에 super().__init__으로 first,last,pay를 받아왔기 때문에 self에는 추가 x """

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang) # Python 

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)



# %%
# class manager 추가 
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

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
      super().__init__(first,last, pay)
      self.employees = [] if employees is None else employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
print(mgr_1.employees)

mgr_1.remove_emp(dev_1)
print(mgr_1.employees)

# %%
