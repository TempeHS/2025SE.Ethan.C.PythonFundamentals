print("What is the Answer to the Great Question of Life?")
B = input()
A = str.casefold(B)
if A == "42" or A == "forty-two" or A == "forty two":
    print("Yes")
else:
    print("No")
