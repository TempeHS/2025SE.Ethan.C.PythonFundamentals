def main():
    Register = input("What's your vanity plate? ")
    if is_valid(Register):
        print("Valid")
    else:
        print("Invalid")


def is_valid(text):
    Chara = 0
    for i in text:
        Chara = Chara + 1
    if Chara >= 6 or Chara <= 2:
        return False
    else:
        for i in text:
            A = Chara - 2
            if str(i).isalpha() is False:
                if str(i).isalnum() is False:
                    return False
            elif str(i).isnumeric():
                a = list(i)
                if str(text[A]).isalpha():
                    return False
                elif a.index("0"):
                    return False
                else:
                    return True
            else:
                return True


main()
