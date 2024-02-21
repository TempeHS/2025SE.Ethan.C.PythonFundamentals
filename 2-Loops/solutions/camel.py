def main():
    name = input()
    B = str.casefold(name)
    A = B.replace(" ", "_")
    print(A)


main()
