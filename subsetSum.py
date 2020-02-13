def SubsetSum(superSet,sum):
	n=len(superSet)
	table = [[0 for x in range(n+1)] for i in range(sum+1)]
	for i in range(n+1):
		table[0][i]=1
	for i in range(sum+1):
		table[i][0]=1
	for i in range(1,sum+1):
		for j in range(n+1):
			table[i][j] = table [i][j-1]
			if (i >= superSet[j-1]):
				table[i][j] = table [i][j] or table[i-superSet[j-1]][j-1]

	print table[sum][n]
	print table


SubsetSum([1,2,3],7)

