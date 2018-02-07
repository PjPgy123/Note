name = "PjPgy"
age = 26
job = "IT"

info1 = '''
************info of {_name} *****************
Name:{_name}
Age:{_age}
Job:{_job}
'''.format(_name=name,_age=age,_job=job)

info2 = '''
************info of {0} *****************
Name:{0}
Age:{1}
Job:{2}
'''.format(name,age,job)

print(info1)
print(info2)