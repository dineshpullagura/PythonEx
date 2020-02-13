def permute (word):
    retList=[]
    if len(word) == 1:
        # There is only one possible permutation
        retList.append(word)
        print (retList)
    else:
        # Return a list of all permutations using all characters
        for pos in range(len(word)):
            # Get the permutations of the rest of the word 
            permuteList=permute(word[0:pos]+word[pos+1:len(word)])
            # Now, tack the first char onto each word in the list
            # and add it to the output
            print ('permuteList',permuteList)
            print ('before for',retList)
            for item in permuteList:
                retList.append(word[pos]+item)
                print ('in for',retList)
    return retList


print (permute('abc'))
