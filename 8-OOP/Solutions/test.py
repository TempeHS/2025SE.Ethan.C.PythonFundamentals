class Student:
    def __init__(self, name, house):  # initilise
        self.name = name  # instance variable 1
        self.house = house  # instance variable 2

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property  # getter (has 1 argument)
    def name(self):
        return self._name  # 1 _ is used for security

    @name.setter  # setter (has 2 arguments)
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @property
    def house(self):
        return self.__house  # 2 _s are used for more security

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.__house = house


def main():
    info = get_info()
    print(info)


def get_info():
    name = input("Name? ")
    house = input("House? ")
    return Student(name, house)  # constructor call instantiates info object


if __name__ == "__main__":
    main()
