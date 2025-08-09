text = input("Enter file name: ")
ntext = open(text)

#empty list named things #things is basically a LIST form of ntext
things = list()

for line in ntext:
    words = line.split()
    
    #removing duplicates 
    for word in words:
        #If the WORD is not on THINGS it will be added if there wont be added
        if word not in things:
            things.append(word)
    
things.sort()    
print(things)
