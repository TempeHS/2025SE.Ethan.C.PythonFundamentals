import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        for row in file:
            print(row.rstrip())
except FileNotFoundError:
    sys.exit("File not found")
