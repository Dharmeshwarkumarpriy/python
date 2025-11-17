print("addition...")
s=lambda a,b,c,d:a+b+c+d
print(s(4,5,6,7))

print("greatest number..")
s1=lambda a,b: a if a<b else b
print(s1(4,3))

print("find odd no b/t 0 to 10...")

print("even or odd...")
# s2=lambda a: a if a%2==0 print(even) else print(odd)
s2=lambda a:"even" if a%2==0 else "odd"
print(s2(5))

