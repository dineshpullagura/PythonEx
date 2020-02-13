def stringPerm(op,ip):
	if not ip:
		print op
	else:
		for i in range(len(ip)):
			next=op+ip[i]
			rem=ip[0:i]+ip[i+1:]
			stringPerm(next,rem)


stringPerm('','abc')
				
