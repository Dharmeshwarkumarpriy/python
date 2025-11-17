s=("hello*python-language-are.you-popular."
   "now-days.what-is*you$price$are you-expansive$ or not")
s1=s.split('-')
for sub in s1:
    print(sub)

s2=s.split('.')
for dot in s2:
    print(dot)

s3=s.split('$')
for dollar in s3:
    print(dollar)

s4=s.split('*')
for star in s4:
    print(star)

# s5=s.split('-,.,$,*')
# for x in s5:
#    print(x)