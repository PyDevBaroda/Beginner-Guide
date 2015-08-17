def person(name,age=22):
	print 'My name is ', name
	print 'my age is ', age
name = raw_input('Enter your name: ')	
person(name)
person(name, age = 23)