'''mylist=[10,20,30]
def changeme(mylist):
	"This changes a passed list into this function"
	mylist.append([1,2,3,4,5]);
	print("Values inside the function:",mylist)
	#return
#mylist=[10,20,30];
changeme(mylist);
print("valuse outside the function:",mylist)'''


def changeme(mylist):
	"This changes a passed list into this function"
	mylist=[1,2,3,4];
	print("Values inside the function:",mylist)
	return
mylist=[10,20,30]
changeme(mylist);
print("Valuse outside the function:",mylist)
