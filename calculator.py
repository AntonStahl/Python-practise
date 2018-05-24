def add(x, y):
	return x + y 
	
def subtract(x, y):
	return x - y
	
def multiply(x, y):
	return x * y 

def divide(x, y):
	return x / y 

print """
1.Add
2.Subtract
3.Multiply
4.Divide
"""	

user_input = raw_input("Chose 1/2/3/4 :")

num1 = int(input("Number :"))
num2 = int(input("Number :"))

if user_input == "1":
	print add(num1, num2)
	
if user_input =="2":
	print subtract(num1, num2)
	
if user_input == "3":
	print multiply(num1,num2)
	
if user_input == "4":
	print divide(num1,num2)

	
