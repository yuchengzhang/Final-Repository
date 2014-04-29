import json

infile = open('data/test.json')
student = json.load(infile)
infile.close()

name = student['name']
grades = student['grades']

print '.' * 70
print name, "got a %d out of %d on lab1" % (grades['lab1']['earned'], grades['lab1']['possible'])
print name, "got a %d out of %d on lab2" % (grades['lab2']['earned'], grades['lab2']['possible'])
print name, "got a %d out of %d on lab3" % (grades['lab3']['earned'], grades['lab3']['possible'])
print '.' * 70