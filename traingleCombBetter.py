
l=[10,21,22,100,101,200,300]
ln=len(l)
l.sort()
count=0


for i in range(0,ln-2):
	k=i+2
	print k
	for j in range(i+1,ln):
 		while (k < ln and l[i]+l[j] > l[k]):
			print l[i],l[j],l[k]
			k+=1
			print "count" + str(count)
			print "i" + str(i) + "j" + str(j) + "k" + str(k)
		count+=k-j-1
print count


	
