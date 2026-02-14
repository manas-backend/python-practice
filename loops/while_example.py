# a=int(input("a = "))
# b=0
# s=1
# while a>0:
#     b=a%10
#     s*=b
#     a//=10
# print(s)
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
