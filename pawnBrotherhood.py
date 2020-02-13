
def safePawns(coord):

	def getCoord(pawn):
		return (ord(pawn[0])-96,int(pawn[1]))
	l=[]
	for i in coord:
		l.append(getCoord(i))
	safe=0
	for i in l:
		if (i[0]-1,i[1]-1) in l or (i[0]+1,i[1]-1) in l:
			safe = safe + 1	
	return safe
	


l=["b4", "c4", "d4", "e4", "f4", "g4", "e5"]
print safePawns(l)
