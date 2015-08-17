import emp_detail
obj1 = emp_detail.Employee("Harsh","Developer")
obj2 = emp_detail.Employee("Dattani","Student")
detail1 = obj1.GetEmpDetail()
detail2 = obj2.GetEmpDetail()
print detail1
print detail2
print 'Total Employees are %d' % emp_detail.Employee.EmpTotal