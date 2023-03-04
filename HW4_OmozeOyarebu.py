"""
Omoze Oyarebu
CS 100 2023S Section 012
HW 04, March 4, 2023

"""
#Exercise 1a
#creates and returns a list of all the strings in strList that end with a letter in Letters.
def hasFinaLLetter(strList,Letters):
    newlist=[]
    for x in strList:
        for y in Letters:
            if (x.endswith(y)):
                newlist.append(x)
    
    return newlist
#1b-Test cases
#1
letters = 'ABCabc'
list = ['Boa','Vate','Yam']
print("hasFinaLLetterTest Case 1:",hasFinaLLetter(list,letters))

#2
letters = 'MLabcT'
list = ['Boa','BalL','YaM','Bob','SweeT']
print("hasFinaLLetter Test Case 2:",hasFinaLLetter(list,letters))

#3
letters = 'BCabc'
list = ['BoA','Vate','Yam']
print("hasFinaLLetter Test Case 3:",hasFinaLLetter(list,letters),"\n")

#Exercise 2a
#create and return a list of all the ints in the range from 1 to maxInt (not including maxInt) that are divisible of both ints in twoInts.
def isDivisible(maxInt,twoInts):
    newlist = []
    for x in range(1,maxInt):
        if ((x % twoInts[0] == 0) and (x % twoInts[1] == 0)):
            newlist.append(x)
    return newlist

#2b-Test cases
#1
tupe=(2,10)
maxint=100
#print("isDivible Test Case 1:")
print("isDivible Test Case 1:",isDivisible(maxint,tupe))

#2
tupe=(4,12)
maxint=100
#print("isDivible Test Case 2:")
print("isDivible Test Case 2:",isDivisible(maxint,tupe))

#3
tupe=(14,9)
maxint=100
#print("isDivible Test Case 3:")
print("isDivible Test Case 3:",isDivisible(maxint,tupe))

