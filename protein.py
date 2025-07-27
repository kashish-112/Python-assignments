text = input("Enter file name: ")
text1 = open(text)
text2 = text1.read()
#print(len(text2))

try:
    protein = text2.split('\n')
    sequence = ''
    for proteins in protein:
        if proteins.startswith('>'):
            continue
        
        sequence += proteins.strip() 

    print(sequence[:78])

except:
    print("Error")                 
