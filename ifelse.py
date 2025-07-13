h = input("Hours of work: ")
r = input("rate: ")
h = float(h)
r = float(r)

if h <= 40:
    pay = h * r
    print(pay)

#o=overtime hours
else:
    o = h - 40
    pay = (40 * r) + (o * r * 1.5)
    print(pay)    
