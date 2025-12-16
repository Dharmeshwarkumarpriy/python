# read and write file 'r+' properties.
g=open('abcd.txt','r+')
data=g.read()
print(data)
# write multiple time after run file.
g.write('i live an tilouthu\n')
g.close()