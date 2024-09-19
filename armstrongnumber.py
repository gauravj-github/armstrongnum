a=111
p=a
i=0
sum=0

while(a>0):
    i=a%10
    sum=sum+(i*i*i)
    a=a//10
if p==sum:
    print("number is armstrong number")
else:
    print("number is not arm strong numnber")
