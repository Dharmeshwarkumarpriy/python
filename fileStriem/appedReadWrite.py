# write and read 'a+' properties.
f=open("abcd.txt","a+")
f.write("i am in delhi \n")
f.seek(0)
print(f.read())
f.close()

