file1=open('example.txt','r')
fileContent=""
for line in file1:
    fileContent +=line
file1.close()
print(fileContent)
print(type(fileContent))