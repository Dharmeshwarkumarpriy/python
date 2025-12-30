from fileStriem.rvision.appendTextToFileDisplay import fileName


def readLastNLines(fileName, n):
    with open(fileName) as file:
        lines=file.readlines()
        lastNlines=lines[-n:]
        for line in lastNlines:
            print(line, end="")

fileName='example.txt'
n=5
readLastNLines(fileName, n)