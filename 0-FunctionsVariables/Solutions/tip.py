def main():  # Main function
    print("How much was the meal?")  # ask for meal price
    D = D_float(input())  # response by user
    print(D)
    print("What percentage would you like to tip?")  # ask for tip (in percent)
    P = D_float(input())  # response by user
    print(P)
    T = D * P  # math for total
    print(f"Leave ${T:.2f}")  # print total


def D_float(D):  # function for price
    str.removeprefix("$")  # idk how to do this
    return float(D)


def P_float():  # function for tip
    str.removesuffix("%")


main()
