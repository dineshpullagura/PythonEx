def RecPermute(soFar,rest):
	if not rest:
		print soFar
			
	else:
		for i in range(len(rest)):
			next=list(soFar)
			next.append(rest[i])
			rem=rest[0:i]+rest[i+1:]
			RecPermute(next,rem)

RecPermute([],[1,2,3])

