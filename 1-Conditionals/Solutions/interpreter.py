A = input()
x, y, z = A.split(" ")
if y == "/" or y == "%":
    print(float(x) / float(z))
elif y == "x" or y == "*":
    print(float(x) * float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "+":
    print(float(x) + float(z))
else:
    print("error")
