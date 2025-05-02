Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> student ={
	'name':'nabeeljavaid',
	'department':'management sciences',
	'section':'c',
	'program':'BBA',
	'age':20,
	'email':'nabeeljavaid175@gamil.com',
	'city':'lahore',
	'religion':'Islam'
	}
>>> print(student)
{'city': 'lahore', 'program': 'BBA', 'religion': 'Islam', 'section': 'c', 'email': 'nabeeljavaid175@gamil.com', 'department': 'management sciences', 'age': 20, 'name': 'nabeeljavaid'}
>>> {'city': 'lahore', 'program': 'BBA', 'religion': 'Islam', 'section': 'c', 'email': 'nabeeljavaid175@gamil.com', 'department': 'management sciences', 'age': 20, 'name': 'nabeeljavaid'}
{'city': 'lahore', 'program': 'BBA', 'religion': 'Islam', 'section': 'c', 'email': 'nabeeljavaid175@gamil.com', 'department': 'management sciences', 'age': 20, 'name': 'nabeeljavaid'}
SyntaxError: multiple statements found while compiling a single statement
>>> print(type(student))
<class 'dict'>
>>> print(student['name'])
nabeeljavaid
SyntaxError: multiple statements found while compiling a single statement
>>> print(student.get('section'))
c
>>> print('f student department is {student.get("department")}')
f student department is {student.get("department")}
>>> student_age = student['age']
>>> print(student_age)
20
SyntaxError: multiple statements found while compiling a single statement
>>> print('dictionary length:',len(student))
dictionary length: 9
>>> student.clear()
>>> print('After clearing:',student)
all_values = student.values()
>>> print(all_values)
dict_values([])
>>> all_values = list(student.values())
>>> print(all_values)
[]
>>> all_values = tuple(student.values())
>>> print(all_values)
()
>>> 
After clearing: {}
