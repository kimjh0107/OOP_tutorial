"""
Property 데코레이터는 내장 함수 property()를 수동으로 호출하지 않고도 쉽게 속성을 정의하는데 도움이 되는 
python의 내장 데코레이터이다. 명시된 getter, setter , deleter에서 클래스의 속성 속성을 매개 변수로 반환하는데 사용됨 
"""

class Employee:
    raise_amount = 1.04 

    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

"""
여기서 우리는 emp_1.first부분을 지정해서 변경해주면 first는 변하지만 email은 변하지 않는 것을 확인 가능 
왜냐하면 run이 돌아가면서 full name method는 grabs the current first anme 
-> 이러한 경우 automatically change 또는 decorator를 사용 
"""
# %%
class Employee:
    raise_amount = 1.04

    def __init__(self,first,last):
        self.first = first
        self.last = last

        # email의 경우 아래에서 따로 지정 -> 위에 decorator property지정 
    @property
    def email(self):
        return f'{self.first} {self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter 
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first 
        self.last = last 

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None 
        self.last = None 

emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Corey Schafer'

emp_1.first = 'Jim'

print(emp_1.last)
print(emp_1.first)
print(emp_1.email)
