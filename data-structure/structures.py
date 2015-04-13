print 'This is the list section'
# defined list colors
colors = ['red','blue','yellow','green','green']

#printing colors lists
print 'First item is',colors[0]

#append an item to end of list
colors.append('black')
print 'Added black to end',colors

#inserting an item at given position
colors.insert(0,'white')
print 'Added white at 0 position',colors

#removes item at given location
print 'Deleted',colors.pop(0),colors

#if nothing is mentioned in pop it will delete last item
colors.pop()
print 'Deleted the last item',colors

#counting number of an item appears in list
print 'Green is repeated',colors.count('green'),' times'

# reverse all elements
colors.reverse()
print 'I am reverse now',colors

#deleting entire list
del colors[:]
print 'I am empty now',colors

print '\n \nThis is the Dictonary section'

#define a Dictionary
marks = {'harsh': '35','manoranjan':'45'}
print marks

#adding value to dictionary
marks['mihir']=20
print 'added mihir in ',marks

#printing specific marks of mihir
print "Mihir's marks are",marks['mihir']

#deleting harsh's marks
del marks['harsh']
print marks

