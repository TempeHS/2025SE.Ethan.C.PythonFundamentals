def main():
    Time = input("What is the time? ")
    convert(Time)


def convert(time):
    h, m = time.split(":")
    mins = float(m) / 60
    hrs = int(h)
    if hrs >= 7 and hrs <= 8:
        print("Breakfeast Time")
    elif hrs >= 12 and hrs <= 13:
        print("Lunch Time")
    elif hrs >= 18 and hrs <= 19:
        print("Dinner Time")
    else:
        print("Nothing")


main()
