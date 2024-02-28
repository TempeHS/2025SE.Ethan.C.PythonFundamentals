def main():
    a = input("What's your tweet? ")
    for i in a:
        if not (i).casefold() in ["a", "e", "i", "o", "u"]:
            print(i, end="")
    print("")


main()
