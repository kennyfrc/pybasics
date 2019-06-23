a = 1
b = 1

print("--------------------------------------")
print("logic and printing")
if a == b:
	print("hello")

print("--------------------------------------")
print("coerce \'2\' to 2")
valtc = "2"
print(int(valtc))

print("--------------------------------------")
print("truthy vs falsy")
if "x":
	print("\"x\" is truthy")
if "":
	print("this shouldn't show up")
else:
	print("\"\" is falsy")
if [1]:
	print("[1] is truthy")
if []:
	print("this shouldn't show up")
else:
	print("[] is falsy")

print("--------------------------------------")
print("looping")
x = 1
for x in [1,2,3,4,5]:
	print("%d Times this has been printed" %(x))

print("--------------------------------------")
print("string interpolation with a basic loop")
y = 1
for x in range(1,6):
  print("%d * %d = %d" %(x, y, x*y))

def fibonacci(num):
	if num < 2:
		return num
	else:
		return fibonacci(num-1) + fibonacci(num-2)

def fibloop(num):
	arr = []
	while num > 0:
		arr.insert(0,fibonacci(num))
		num -= 1
	print(arr)
	return arr

print("--------------------------------------")
print("fibonacci (recursion)")
fibloop(15)

print("--------------------------------------")
print("since python is pass by object reference, you need to make a copy")

name = ["Kenn"]

def hello(name):
	name = name[:]
	name.append("Francis")
	print("Name inside function: %s" %(name))

hello(name)

print("This should not have been modified: %s" %(name))
print("--------------------------------------")

name2 = ["Kenn"]

def hello2(name):
	name.append("Francis")
	print("Name inside function: %s" %(name))

hello2(name2)

print("This should have been modified: %s" %(name2))

print("--------------------------------------")
print("map, filter, reduce with anon/lambda functions")
print("map [1,2,3] by x ** 2")
print(list(map(lambda x: x ** 2, [1,2,3])))
print("filter [1,2,3] by x <2 ")
print(list(filter(lambda x: x < 2, [1,2,3])))
print("reduce [1,2,3] by x * y ")
from functools import reduce
print(reduce(lambda x, y: x * y, [1,2,3]))

print("--------------------------------------")
print("function definition order matters")




