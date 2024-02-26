def main():
    camelcase(input("What's your name in camel case? "))
    print(" ")


def camelcase(txt):
    for i in txt:
        if (i).isupper():
            print("_" + i.casefold(), end="")
        else:
            print(i, end="")


main()
