from fileStriem.rvision.readLineByLine import fileName


def readFileToList(fileName):
    lines=[]
    with open(fileName,'r')as file:
        while True:
            line=file.readline()
            if not line:
                break
            lines.append(line.strip())
    return lines

fileName='example.txt'
a=readFileToList(fileName)
print(a)
print(type(a))
print(type(fileName))