import emoji


def main():
    A = input("What is your emoji? ")
    B = emoji.emojize(A, language="alias")
    print(B)


main()
