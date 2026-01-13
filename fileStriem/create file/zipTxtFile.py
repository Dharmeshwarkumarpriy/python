from zipfile import *

f=ZipFile("dharamTxtFile.zip",'w',ZIP_DEFLATED)
f.write('abcd.txt')
f.write('abcf.txt')
f.write('../abc.txt')

f.close()
print('file zipped successfully')