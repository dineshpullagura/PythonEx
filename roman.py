def checkio(num):
	roman = {}
    	roman[1000] = "M"
    	roman[900] = "CM"
    	roman[500] = "D"
    	roman[400] = "CD"
    	roman[100] = "C"
    	roman[90] = "XC"
    	roman[50] = "L"
    	roman[40] = "XL"
    	roman[10] = "X"
    	roman[9] = "IX"
    	roman[5] = "V"
    	roman[4] = "IV"
    	roman[1] = "I"
    	#replace this for solution
    	rom=''
	l=sorted(roman.keys(),reverse=True)
	while num>0:
        	for i in l:
       			if num >= i:
              			rom += roman[i]
              			num -= i
				break
	print rom
checkio(123)		
