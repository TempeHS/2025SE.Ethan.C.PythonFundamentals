def main():  # Main function
    print("How much was the meal?")  # ask for meal price
    D = D_float(input())  # response by user
    print("What percentage would you like to tip?")  # ask for tip (in percent)
    P = P_float(input())  # response by user
    T = D * P  # math for total
    print(f"Leave ${T:.2f}")  # print total


def D_float(d):  # function for price
    d = d.replace("$", " ")  # removes $
    d = float(d)  # stores as float
    d = round(d, 2)  # rounds to 2 dp.
    return d


def P_float(p):  # function for tip
    p = p.replace("%", "")  # removes %
    p = float(p)  # stores as float
    p = p / 100  # to decimal
    return p


main()
