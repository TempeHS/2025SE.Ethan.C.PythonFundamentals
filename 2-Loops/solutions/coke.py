def main():
    c = 50
    a = insert(input("Do you want a coke for 50c? "))
    b = int(c - a)
    if b > 0:
        print(f"Amount Due {b: }")
    elif b < 0:
        print(f"Change owed {b: }")


def insert(a):
    a = input("5c, 10c or 25c ")
    if a == 5 or 10 or 25:
        return int(a)
    if a != 5 or 10 or 25:
        input("Try again ")


main()
