from PyOOPTask import Shape


def main():
    while True:
        print(assessInput(input("")))


def assessInput(method):
    if method == "Position":
        return Shape.VECTOR
    if method == "Info":
        return Shape.INFO


if __name__ == "__main__":
    main()
