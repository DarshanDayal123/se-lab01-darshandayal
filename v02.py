#calculator in python(v0.2) 

def add(num1,nun2):
	return num1+num2 

def sub(num1,num2):
	return num1-num2

def mul(num1, num2):
	return num1 * num2

#main
num1 = int(input("Enter the 1st num: "))
num2 = int(input("Enter the 2nd num: "))

res = add(num1,num2)
print(res)
print(sub(num1,num2))
print(mul(num1,num2))