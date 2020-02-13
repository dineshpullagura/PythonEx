def RecPermute(soFar,rest):
	if not rest:
		print soFar
			
	else:
		next=list(soFar)
		next.append(rest[0])
		RecPermute(next,rest[1:])
		#print next, rest[1:],soFar
		RecPermute(soFar,rest[1:])

RecPermute([],[1,2,3])

