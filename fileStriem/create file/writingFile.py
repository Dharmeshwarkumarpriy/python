# ............. writing data to text file ..............
# we can write character data to the text file using following two methods.
# write(str).
# write lines(list of lines).

f=open("abcd.txt",'w')
f.write("hello \n")
list=['sam\n','sir\n',"good morning"]
f.writelines(list)
print("write lines")
f.close()