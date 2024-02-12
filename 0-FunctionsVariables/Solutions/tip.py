def main():  # Main function
    print("How much was the meal?")  # ask for meal price
    D = D_float(input())  # response by user
    print(D)
    print("What percentage would you like to tip?")  # ask for tip (in percent)
    P = D_float(input())  # response by user
    print(P)
    T = D * P  # math for total
    print(f"Leave ${T:.2f}")  # print total


def D_float(d):  # function for price
    d = d.replace("$", " ")
    d = float(d)
    d = round(d, 2)
    return d


def P_float(p):  # function for tip
    p = p.replace("%", " ")
    p = float(p)
    p = p / 100
    return p


main()
