import random
class Employee(object):
	'Common class for all Employees'
	EmpId = 0
	EmpTotal = 0

	def __init__(self,name,post):
		self.name = name
		self.post = post
		self.EmpId = random.randint(0,9)
		Employee.EmpTotal += 1

	def GetEmpDetail(self):
		return (self.EmpId, self.name,self.post)

obj1 = Employee("Harsh","Developer")
obj2 = Employee("Dattani","Student")
detail1 = obj1.GetEmpDetail()
detail2 = obj2.GetEmpDetail()
print detail1
print detail2
print 'Total Employees are %d' % Employee.EmpTotal