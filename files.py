text = input("Enter a file name: ")
text1 = open(text)

#see the for and in thingy carefully. 
#here lines is the iteration variable. so basically the data in text1 will be assigned to lines
for lines in text1:
    print(lines.upper().strip())
     


