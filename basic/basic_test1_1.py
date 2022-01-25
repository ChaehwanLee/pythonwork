# #print('test1')
# import random
# num1 = random.choice([1,2,3,4,5,6,7,8,9,10])
# num2 = random.choice([1,2,3,4,5,6,7,8,9,10])
# result = num1 + num2
#
# print('num1=',num1)
# print('num2=',num2)
# #print('result=',result)
# #print("더한결과=",result)
# print("result=",(num1+num2))


import random
num1 = random.choice([1,2,3,4,5,6])
num2 = random.choice([1,2,3,4,5,6])
result = num1+num2
print("num1=", num1)
print("num2=", num2)
print("result=", result)
print("result=", num1+num2)
print("result=", num1+num1)


num2 = 3
result = 8
result = 8
num1 = 5
result = 10
num1 = input("num1:")
num2 = input("num2:")
print("num1+num2=", num1+num2)

#print 에서 문자와 숫자를 연결해서 사용 할 수 없다 그래서 그래서 숫자를 문자로 변경해줌
#문자열을 숫자열로 변경하는 작업을 해줘야한다
#들여쓰기를 잘해야한다

#Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
#[Clang 6.0 (clang-600.0.57)] on darwin
#Type "help", "copyright", "credits" or "license()" for more information.
#>>> import random
#>>> num1 = random.choice([1,2,3,4,5,6])
#>>> num2 = random.choice([1,2,3,4,5,6])
#>>> result = num1+num2
#>>> print("num1=", num1)
#num1= 6
#>>> print("num2=", num2)
#num2= 4
#>>> print("result=", num1+num2)
#result= 10
#>>> num1 =5
#>>> num2 =3
#>>> result =8
#>>> result =8
#>>> result =10
#>>> 
#====== RESTART: /Users/r/Desktop/2022_iot/Work/pythonwork/basic_test1_1.py =====
#num1= 4
#num2= 3
#result= 7
#result= 7
#result= 8
#num1:100
#num2:200
#num1+num2= 100200
#>>> num1 = int(input("num1:"))
#num1:100
#>>> num2 = int(input("num2:"))
#num2:200
#>>> num1+num2
#300
#>>> num1 = input("num1:")
#num1:100
#>>> type(num1)
#<class 'str'>
#>>> num2 = 200
#>>> type(num2)
#<class 'int'>
#>>> num3 = 10.4
#>>> num3
#10.4
#>>> type(num3)
#<class 'float'>
#>>> 2+4
#6
#>>> 2*4
8
>>> 2-1
1
>>> 30/4
7.5
>>> 30%4
2
>>> print("num1\num2")
num1
um2
>>> print("num1\nnum2")
num1
num2
>>> print('num1')
num1
>>> print('''
		test
		test2
		test3
		test4
		''')

		test
		test2
		test3
		test4
		
>>> 2*6
12
>>> 2+5*5
27
>>> (2+5)*5
35
>>> 2+
SyntaxError: invalid syntax
>>> 'hot'*5
'hothothothothot'
>>> num1 = 100
>>> print(num1)
100
>>> print(num1, num1, num1, num1)
100 100 100 100
>>> print(num1, str1)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(num1, str1)
NameError: name 'str1' is not defined
>>> str1 = "test"
>>> print(num1, str1)
100 test
>>> print("num1"+num1+"str1"+str1)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print("num1"+num1+"str1"+str1)
TypeError: can only concatenate str (not "int") to str
>>> print("num1"+str1+"str1"+str1)
num1teststr1test
>>> print("num1"+str(num1)+"str1"+str1)
num1100str1test
>>> 	print("num1")
	
SyntaxError: unexpected indent
>>> 
