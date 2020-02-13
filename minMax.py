def min(*args, **kargs):
	
	if len(args)==1: args=list(args[0])
	key = kargs.get('key',None)
	result = args[0]
	for i in range(1,len(args)):
		result=minSimple(result,args[i],key)
		print result,i
	return result

def minSimple(a,b,key):
	if key!=None and int(b) < int (a):
		return b
	if key == None and b < a:
		return b

	return a

def max(*args, **kargs):

        if len(args)==1: args=list(args[0])
        key = kargs.get('key',None)
        result = args[0]
        for i in range(1,len(args)):
                result=minSimple(result,args[i],key)
                print result,i
        return result

def maxSimple(a,b,key):
        if key!=None and int(b) < int (a):
                return b
        if key == None and b < a:
                return b

        return a


print min(1,2,3,4,key=None)
