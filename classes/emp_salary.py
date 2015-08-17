import emp_detail
class Salary (emp_detail.Employee):
	def __init__(self):
		print 'emp_detail class called'
		print 'Total Employees are %s' % emp_detail.Employee.EmpTotal