introsString=input("enter your introduction")
#print (introsString)

characterCount=0
wordCount=1
for i in introsString:
    characterCount=characterCount+1
    #print(characterCount)
    if(i==' '):
        wordCount=wordCount+1
print("no of words in the string")
print(wordCount)
print("no of characters in the string")
print(characterCount)