
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

#    def __repr__(self):
 #       return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

#    def __str__(self):
  #      pass


emp_1=Employee('badmash','billu',60000)
emp_2=Employee('bagad','billa',2000)

print(emp_1)
