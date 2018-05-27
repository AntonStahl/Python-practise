class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.'+ last + '@bla.com'
	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	
	
#before adding stuff to the class(init func)
emp_1 = Employee('Cory', 'Barlog', 75000)
emp_2 = Employee('Hannes', 'Hennes', 40000)

print(emp_1)
print(emp_2)

emp_1.first = 'Cory'
emp_1.last = 'Barlog'
emp_1.email = 'Cory.Barlog@bla.com'
emp_1.pay = 75000

emp_2.first = 'Hannes'
emp_2.last = 'Hennes'
emp_2.email = 'Hannes.Hennes@bla.com'
emp_2.pay = 40000

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())
