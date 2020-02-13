import sys

def findPrime(n):
	primes=[]
	isPrime=[0,0]+[1]*(n-1)
	for p in range(2,n+1):
		print isPrime
		if(isPrime[p]):
			primes.append(p)
		for i in range(p,n+1,p):
			isPrime[i]=0
   	print primes	

findPrime(10)
