def main():
    input("Do you want a coke for 50c? ")
    c = 0
    b = insert(c)
    if b < 0:
        print(f"Change owed {-b: }")
    else:
        print(f"Amount due {b:}")


def insert(c):
    c = 50
    while c > 0:
        a = int(input("5c, 10c or 25c "))
        if a == 5 or a == 10 or a == 25:
            b = c - a
            if b > 0:
                print(f"Amount Due {b: }")
                c = b
            elif b <= 0:
                return b
        elif a != 5 or 10 or 25:
            print(f"Amount Due {c: }")


main()
