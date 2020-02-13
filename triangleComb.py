
l=[10,21,22,100,101,200,300]
ln=len(l)
count=0

def checkTriangle(a,b,c):
	if (a+b > c and b+c > a and c+a > b):
		return True

for i in range(0,ln):
	for j in range(i+1,ln):
		for k in range(j+1,ln):
			if(checkTriangle(l[i],l[j],l[k])):
				count=count+1

print count


	
