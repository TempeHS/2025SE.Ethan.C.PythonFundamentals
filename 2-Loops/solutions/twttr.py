def main():
    convert(input("What's your tweet? "))

    def convert(text):
        str.casefold(text)
        for i in text:
            if i.isvowel():
                print("" + i, end="")
            else:
                print(i, end="")

        def isvowel(text):
            for a in text:
                return True
            for e in text:
                return True
            for i in text:
                return True
            for o in text:
                return True
            for u in text:
                return True


main()
