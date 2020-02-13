A=[2,2,6,0,0,0]
B=[2,4,6]
m=3
n=3
i=n-1
j=m-1
x=m+n-1
while(i>=0 and j>=0):
	if(A[i]>B[j]):
		A[x]=A[i]
		x=x-1
		i=i-1
	elif A[i]==B[j]:
		i=i-1
		j=j-1
	else:
		A[x]=B[j]
		x=x-1
		j=j-1

if (A[0]>=B[0]):A[0]=B[0]

print A
	
