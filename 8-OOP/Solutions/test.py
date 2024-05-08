class Student:
    def __init__(self, name, house):  # initilises an object
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Missing House")
        self.name = name  # instance variable 1
        self.house = house  # instance variable 2

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    info = get_info()
    print(info)


def get_info():
    name = input("Name? ")
    house = input("House? ")
    return Student(name, house)  # constructor call instantiates info object


if __name__ == "__main__":
    main()
