def readFileTolist(fileName):
    lines=[]
    with open(fileName,'r') as file:
        while True:
            line=file.readline()
            if not line:
                break
            lines.append(line.strip())
    return lines


fileName="example.txt"
a=readFileTolist(fileName)
print(a)