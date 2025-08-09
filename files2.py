text = input("Enter file name: ")
text1 = open(text)
count  = 0
total = 0.0

for line in text1:
    #find the lines containing xdspam...
    if line.startswith("X-DSPAM-Confidence: "):
       # in those lines find the position of :
        fp = line.find(":")

        #now in fp extract the parts 1 step after: and convert those to float and remove white space using .strip()
        nos = float(line[fp+1:].strip())

        #+= is a way of telling to add all the numbers 
        total += nos
        count = count + 1
avg = total / count

print('Average spam confidence:', avg)
