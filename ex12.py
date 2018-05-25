elem = str(raw_input("Enter Word or Sentence:"))

rvs = elem[::-1]
print(rvs)
if elem == rvs:
	print"It's a palidrome"
	
else:
	print"It's not a palidrome"