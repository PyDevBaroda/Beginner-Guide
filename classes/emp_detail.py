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