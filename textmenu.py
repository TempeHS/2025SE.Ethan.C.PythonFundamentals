h = True
while h == True:
    print("Option 1 or Option 2 or Option 3 or Exit")
    A = input()
    if A == "Option 1" or A == "Option 2" or A == "Option 3":
        h = True
    elif A == "Exit":
        h = False
    else:
        print("syntax error")
        h = True
