from datetime import date
import sys


class vsauce:
    def __init__(self, DoB):
        self.DoB = DoB

    def __str__(self, DoB, DoT):
        print(f"{DoT} - {DoB}")

    @property
    def DoB(self):
        return self._DoB

    @DoB.setter
    def DoB(self, DoB):
        if not DoB:
            sys.exit("Missing Name")
        elif str(DoB).find("-") is False:
            sys.exit("Missing Syntax")
        else:
            return DoB


def main():
    GAA = kys(vsauce.Balls(DoB=input("What is your date of birth? ")))
    DoT = date.today()
    print(f"{GAA} ############ {DoT}")
    # vsauce(DoB, DoT)


def kys(BOO):
    return date(BOO).strftime()


if __name__ == "__main__":
    main()
