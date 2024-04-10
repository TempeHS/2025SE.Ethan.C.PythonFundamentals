cart = {}

while True:
    try:
        item = input().upper()
        if item in cart:
            cart[item] = +1
        else:
            cart[item] = 1

    except EOFError:
        break

for item in sorted(cart.keys()):
    print(cart[item], item)
