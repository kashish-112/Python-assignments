text = open("mbox-short.txt")
bw = None
bc = None
emplist = dict()

for email in text:
    if not email.startswith("From "):
        continue
    mail = email.split()

    #taking the 1 value which is email adress
    name = mail[1]
    #adding that to the empty dictionary
    emplist[name] = emplist.get(name, 0) + 1
    

for word, count in emplist.items():
    if bc is None or bc < count:
        bw = word
        bc = count

print(bw, bc)