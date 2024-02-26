def main():
    Time = input("What is the time? ")
    convert(Time)


def convert(time):
    h, m = time.split(":")
    mins = float(m) / 60
    hrs = int(h)
    time = hrs + mins
    if time >= 7 and time <= 8:
        print("Breakfeast Time")
    elif time >= 12 and time <= 13:
        print("Lunch Time")
    elif time >= 18 and time <= 19:
        print("Dinner Time")
    else:
        print("Nothing")


main()
