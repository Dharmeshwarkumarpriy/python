from zipfile import *

f=ZipFile("D:/All pdf/dhram/photo/dharam.zip",'w',ZIP_DEFLATED)
f.write('2022.jpg')
f.write('friend.jpg')
f.write('sunLight.jpg')
f.write("sunSet.jpg")
f.write("bike.jpeg")
f.write('newdk.jpg')
f.write('D:/All pdf/dhram/hi.jpg')
f.write("D:/All pdf/dhram/nature.jpeg")
f.close()
print('file zipped successfully')