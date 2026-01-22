def appendTextToFile(fileName, text):
    with open(fileName,'a') as file:
        file.write(text+'\n')
def displayFileContent(fileName):
    with open(fileName,'r') as file:
        fileContent=file.read()
    print(fileContent)
fileName="example.txt"
textToAppend="this is the new text to append."
appendTextToFile(fileName, textToAppend)
displayFileContent(fileName)