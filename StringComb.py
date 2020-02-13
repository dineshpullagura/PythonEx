def recComb(ip,op):
	if not op:
		print ip
	else:
		recComb(ip+op[0],op[1:])
		recComb(ip,op[1:])


recComb('','abc')
