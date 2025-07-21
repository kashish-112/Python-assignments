largest = None
smallest = None

while True:
    nos = input("Please enter an integer value: ")
    #print(nos)
    if nos == "done":
            break
    
    try:
        nos = int(nos)
        
    except: 
        print("Invalid input")
        continue
        
    if largest is None:
        largest = nos
    elif nos > largest:
        largest = nos
        
        
    if smallest is None:
        smallest = nos
    elif nos < smallest:
        smallest = nos

print("Maximum is", largest )
print("Minimum is", smallest )