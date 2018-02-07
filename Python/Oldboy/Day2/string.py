# -*- coding: utf-8 -*-
"""-------------------------------------------------
   File Name：     string
   Description :
   Author :        PjPgy
   date：          2018/1/28 0028
-------------------------------------------------"""

name = "my  \t name is {name} and i am {age} year old"
print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))
print(name.endswith("ex"))
print(name.expandtabs(tabsize=30))
print(name[name.find("m"):10])
print(name.format(name="alex",age=33))
print(name.format_map({'name':'alex','age':12}))
print("ab123".isalnum())
print("ab123A".isalpha())
print("1A".isdecimal())
print("12".isdigit())
print("_a".isidentifier()) #判断是不是一个合法的标识符
print("a".islower())
print("12".isnumeric())
print(" ".isspace())
print("My Name Is :".istitle())
print("My Name Is :".isprintable()) #tty file ,drive file
print("MY :".isupper())
print('+'.join(['1','2','3']))
print(name.ljust(50,"*"))
print(name.rjust(50,"*"))
print("Alex".lower())
print("Alex".upper())
print("\nAlex".lstrip())
print("-----")
print("Alex\n".rstrip())
print("-----")
print("\nAlex\n".strip())
print("-----")

p = str.maketrans("abcdef","123456")
print("alex li".translate(p))

print('alex li'.replace('l','L',1))
print('1+2+3+4'.split('+'))
print('1+2\n3+4'.splitlines())

print("PjPgy".swapcase())

print("pj pgy".title())

print("pj pgy".zfill(50))