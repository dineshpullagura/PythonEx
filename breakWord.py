l=['i','apple','pie','eat']

word='eatiapplepie'

def breakWord(word,l):
	for i in range(len(word)+1):
		s= word[:i]
		print s
		if s in l:
			res=breakWord(word[i:],l)
			if res != '':
				return s + " " + res

	if s in l:
		print s
		return s
	
	return ''


print breakWord(word,l)
