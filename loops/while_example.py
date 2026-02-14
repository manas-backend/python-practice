a=int(input("a = "))
b=0
s=1
while a>0:
    b=a%10
    s*=b
    a//=10
print(s)