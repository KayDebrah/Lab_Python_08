import re


def isEmail(inp):
    return re.match(r'(\w)+@\w+(\.\w)',inp)!=None
    #return re.match(r'(\w)+@\w+(\.\w){2,4}+',inp)!=None



email=raw_input("Enter Email: ")

print isEmail(email)


def getTxts(inp):
    #find the words with extension .txt
    return re.findall(r'\w+\.txt\s',inp)

print getTxts('yo.html blah.txt woah.txt he ')


def percAwesome(inp):
    #find the number of either awesome or awes0me occurrebces in the string
    num_awe=re.findall(r'awesome|awes0me',inp)
    #find the number of worda ind string
    num_words=re.findall(r'\w+',inp)
    
    #the length of  total number of words
    totalnum=float(len(num_words))
    #the length of  awesome or awes0me in the string
    totalawe=float(len(num_awe))

    #calculate the percentage 
    percentage=(totalawe/totalnum)*100
    #print 
    print 'The percentage of awesomeness in : ',inp, "is:",percentage
    
    
print percAwesome('iamawesomeblah and awes0me is as awesomeo does')

print percAwesome('hello my name is wayawesomedude')




