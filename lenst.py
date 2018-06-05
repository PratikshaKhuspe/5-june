def st():
	s1=str(input("Enter the string:"))
	s2=str(input("Enter the string:"))
	if(len(s1)>len(s2)):
		return s1
	elif (len(s1)==len(s2)):
		print("Both strings are equal\n",s1,"\n",s2)
	else:
		return s2
print("The string is:",st())

