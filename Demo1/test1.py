import math
import re

list = ['Jan','Feb']
print list[0]
list[0] = 'Monday'
print list

database=[['afsdfas','12334'],['fjj','510'],['father','512'],['test','310']]

username = raw_input('user name:')
pin = raw_input("code:")
if [username,pin] in database:
    print "sucess"
else:
    print 'fail'
print len(database)


