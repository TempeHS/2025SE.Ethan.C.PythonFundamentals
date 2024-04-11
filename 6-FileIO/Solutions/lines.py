n = 0

with open("_.py") as file:
    for line in file:
        if line.rstrip().startswith("#") is True:
            pass
        else:
            n = n + 1
    print(f"{n}")
