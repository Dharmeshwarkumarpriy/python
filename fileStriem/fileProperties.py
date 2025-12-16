#... various properties of file object .....
# once we opened a file and we got file object, we can get various details related to that file by using its properties.
# name:- name of opened file.
# mode:- mode in which file is opened.
# closed:- return boolean value true if file is closed.
# readable():- if file is readable then give true boolean value.
# writable():- if file is writable then give true boolean value otherwise false.

f=open("abcd.txt",'w')
print("file name=",f.name)
print('file mode=',f.mode)
print('is file closed?=',f.closed)
print('is file readable?=',f.readable())
print("is file writable?=",f.writable())
f.close()
print('is file closed?=',f.closed)