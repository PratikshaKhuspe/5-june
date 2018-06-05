total=0      #global variable

def sum(a1,a2):
	total=a1+a2;                                             #local variable
	print("Inside the function local total:",total)
	return total;
sum(10,20);
print("Outside the function global total:",total)
