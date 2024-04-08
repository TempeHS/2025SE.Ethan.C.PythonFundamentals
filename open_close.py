with open("myText.txt", "r+t") as file:  # open file
    eLine = file.read()  # read each line of file as eLine
    file.write(int(eLine) + 1)  # write the increment of each line

file.close()
