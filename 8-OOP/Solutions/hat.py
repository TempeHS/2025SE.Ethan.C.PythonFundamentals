import random


class Hat:
    house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Syltherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.house))


def main():
    Hat.sort(input())


if __name__ == "__main__":
    main()
