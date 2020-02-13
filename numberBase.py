def chartoint (c):
	return ord(c) - ord("A") + 10 if c.isalpha() else int(c)


def baseConversion(numStr,radix):
	result=0
	for i,char in enumerate(reversed(numStr)):
		res = chartoint(char)

		if res>radix:
			return -1

		result = result + res * radix ** i

	return result

print baseConversion('AF',16)




