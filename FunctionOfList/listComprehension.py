s=[x*x for x in (range(1,11))]
print(s)
even=[x for x in s if x%2==0]
print(even)
odd=[x for x in s if x%2!=0]
print(odd)