def main():
    x = int(input("What is x? "))  # ask for x
    if x_even(x):  # function
        print("Even")
    else:
        print("Odd")


def x_even(n):
    return n % 2 == 0
    # check for n mod 2 = 0


main()
