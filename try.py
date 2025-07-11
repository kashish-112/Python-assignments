s = input("Your score: ")
try:
    s = float(s)

    if s > 1:
        print("Please enter a value in the given range")

    elif s >= 0.9:
        print("A")

    elif s >= 0.8:
        print("B")

    elif s >= 0.7:
        print("C")

    elif s >= 0.6:
        print("D")

    elif s < 0.6:
        print("F")
except:
    print("Please enter a numerical value")



            

