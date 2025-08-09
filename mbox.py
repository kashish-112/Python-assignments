text = open("mbox-short.txt")
count = 0
for email in text:
    if email.startswith("From:"):
        continue
    elif email.startswith("From"):
        mail = email.split()
        print(mail[1])
        count= count + 1
#adding f otherwise print wont recognise {} it will print 
#There were {count} lines in the file with From as the first word instead of 27 at the place of {count}
print(f"There were {count} lines in the file with From as the first word")

