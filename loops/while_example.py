# 5.
a=int(input("a = "))
b=0
s=1
while a>0:
    b=a%10
    s*=b
    a//=10
print(s)
# 6.
a=int(input("a = "))
c=a
b=0
sum=0
while a>0:
    b=a%10
    sum+=b
    a//=10
if sum%len(str(c))==0:
    print(True)
else: print(False)
# 7.
a=int(input("a = "))
plus=0
minus=0
while a!=0:
    if a>0:
        plus+=1
    else:
        minus+=1
    a=int(input("a = "))
print("Musbat sonlar:", plus)
print("Manfiy sonlar:", minus)
# 8.
a=int
s=0
while a!=0:
    a=int(input("a = "))
    if a%2!=0:
        s+=a
print("Toq sonlar yig'indisi:", s)
# 9
a=int(input("N = "))
b=1
c=0
i=0
while a>i:    
    print(c,end=" ")
    c,b=b,b+c
    i+=1
# 10.
a=int(input("a = "))
i=1
while i<=a:
    print(i*i,end=", ")
    i+=1
# 1.
number=1
while number<=10:
    print(number,end=", ")
    number+=1
# 2.
a=int(input("a = "))
i=1
while i<=10:
    print(f"{i}*{a}={i*a}")
    i+=1
# 3.

i=1
while i<=20:
    if i%2==0:
        print(i,end=", ")
    i+=1
# 4.
i=1
while i<=20:
    if i%2!=0:
        print(i,end=", ")
    i+=1
# 5.
a=int(input("a="))+1
b=int(input("b="))
sum=0
while a<b:
    sum+=a
    a+=1
    print(a)
print(sum)
# 6.
a=int(input("a="))+1
b=int(input("b="))
kopayt=1
while a<b:
    kopayt*=a
    a+=1
print(kopayt)
# 7.
a = int(input("a = "))+1
b = int(input("b = "))
i = a + 1   
while a < b:
    if a % 2 == 0:
        print(a)
    a += 1
# 8.
a=int(input("a="))+1
b=int(input("b="))
while a<b:
    if a%2==1:
        print(a)
    a+=1
# 9.
a=int(input("a="))+1
b=int(input("b="))
sum=0
k=1
while a<b:
    if a%2==0:
        sum+=a
        a+=1
    else:
        k*=a
        a+=1
        
print("summa",sum,"\nkopaytma",k)
# 10.
n = int(input("N=: "))
i = 1
while i<=n:
    if n%i==0:
        print(i)
    i+=1
# 11.
n=int(input("N= "))
i=1
k=0
sum=0
while i<=n:
    k+=i
    if n%i==0:
        sum+=i
    i+=1
print(k-sum)
# 12.
a=int(input("a="))
i=1
sum=0
while i<a:
    if a%i==0:
        sum+=i
        print(i)
    i+=1
if sum==a:print("mukammal son")
else:print("mukammal emas")
# 13.
a=int(input("a="))
i=a
sum=0
while i>0:
    b=i%10
    sum+=b
    i//=10
print(sum)