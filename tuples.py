text = open("mbox-short.txt")
count = 0
chrs = dict()


for email in text:
    if not email.startswith("From "):
        continue

    mail = email.split()
    #taking the 5th value which is time
    time = mail[5]
    #spliting again and addig only hour to the dictionary
    hour = time.split(':')[0]

    chrs[hour] = chrs.get(hour, 0) + 1

#sorting plus creating tuple
for hours, count in sorted(chrs.items()):
    print(hours, count)


    

