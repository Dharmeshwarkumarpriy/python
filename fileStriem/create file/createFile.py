# crate file using 'x' properties.
f=open('abcf.txt', 'x')
f.write("Testing x mode")
f.close()

#..... closing file .........
# after completing our operations on the file it is highly recommended to close the file.
# for this we have to use close() functon.
# f.close()