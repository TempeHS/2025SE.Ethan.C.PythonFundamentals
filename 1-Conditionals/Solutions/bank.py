input = input()
greeting = str.casefold(input)
if "hello" in greeting:
    print("$0")
elif str(greeting).startswith("h"):
    print("$20")
else:
    print("$100")
