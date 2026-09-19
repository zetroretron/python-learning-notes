class Employee:
    raise_amount=1.04
    num=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@gmail.com'

        Employee.num+=1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last)

    def __str__(self):
        pass
'''
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt= amount
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first, last, pay)
    

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
'''
'''
#inheritance
class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        #or
        #Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
            else:
                self.employees = employees

'''



emp_1=Developer('badmash','billu',60000)
emp_2=Developer('bagad','billa',2000)

print(emp_1)
repr(emp_1)
str(emp_1)
'''
dev_1=Developer('bodam','billa',600, 'PYTHON')


print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.num)

emp_str_1 = 'david-dhawan-20000'


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)


import datetime
my_date = datetime.date(2026, 8, 16)
print(Employee.is_workday(my_date))
'''

