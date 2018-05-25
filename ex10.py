num = int(raw_input("Enter a number:"))

for i in range(1,num+1,1):
	x = i
	y = num % i 
	if y == 0:
		print x 