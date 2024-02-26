def main():
    text = input("What's your tweet? ")
    post = TWITTER(text)
    print(post)

    def TWITTER(text):
        UMAC = str.upper(text)
        if "A" in UMAC:
            print(text, end="")
        if "E" in UMAC:
            print(text, end="")
        if "I" in UMAC:
            print(text, end="")
        if "O" in UMAC:
            print(text, end="")
        if "U" in UMAC:
            print(text, end="")


main()
