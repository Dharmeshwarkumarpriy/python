def separateCharactersByComma(fileName):
    with open(fileName)as file:
        content=file.read()
    separatedContent=','.join(content)

    with open(fileName,"w") as file:
        file.write(separatedContent)

fileName="example.txt"
separateCharactersByComma(fileName)