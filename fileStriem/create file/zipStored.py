from zipfile import ZIP_STORED, ZipFile

f=ZipFile("dharamTxtFile.zip",'r',ZIP_STORED)
names=f.namelist()
for name in names:
    print("file name",name)
    print("the content fo file is....")
    f1=open(name,'r')
    print(f1.read())
    print()