def main():
    while True:
        try:
            item = input()
            menu[item]
        except EOFError:
            print("Error")
        else:
            break

    if item in menu:
        bill = 
        print(f"{bill}")

main()

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
