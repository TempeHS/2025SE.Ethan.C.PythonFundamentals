from pyfiglet import Figlet
import sys
import random


figlet = Figlet()


def main():
    A = input("What would you like to figletise? ")
    figlet.getFonts()
    f = input("What is your font? ")
    if str.isnumeric(f) is True:
        f = float(f)
    else:
        f = str(f)
    if f == 0:
        f = random.choice(figlet.getFonts())
        figlet.setFont(font=f)
        print(figlet.renderText(A))
    elif f.isalpha() is True:
        figlet.setFont(font=f)
        print(figlet.renderText(A))
    else:
        print(sys.exit)


main()
