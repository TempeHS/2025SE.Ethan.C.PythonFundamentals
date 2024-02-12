print("What is the Answer to the Great Question of Life?")
A = input()
A = A.casefold(A)
if A == "42":
    print("Yes")
 elif A == "forty two":
    print("Yes")
else:
    print("No")
