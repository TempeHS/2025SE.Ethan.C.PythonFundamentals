def main():
    H = input("Gauge? ")
    while True:
        try:
            X, Y = H.split("/")
            X = int(X)
            Y = int(Y)
            fuel = (X / Y) * 100
        except (ValueError, ZeroDivisionError):
            print("Error")
        else:
            break

    f = round(fuel)
    if f < 1:
        print("E")
    elif f > 99:
        print("F")
    else:
        print(f"{f}%")


main()
