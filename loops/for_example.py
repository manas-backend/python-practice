# 1.
# for i in range (1,11):
#     print(i,end=" ")
# 2.
# N=int(input("N= "))
# a=0
# for i in range(1,N):
#     a+=i
#     print(a)
# 3.
# n=int(input("N= "))
# a=0
# for i in range(1,n):
#     if i%2==0:
#         a+=i
#     print(a)
# 4.
# n=int(input("N= "))
# a=0
# b=0
# for i in range(1,n):
#     if i%2==0:
#         a+=i
#     b+=i
# print(b-a)
# 5.
# n=int(input("N= "))
# for i in range (1,11):
#     print(f"{i}*{n}={i*n}")
# 6.
# for i in range(1,11):
#     print(i*i)
# 7.
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(b-1,a,-1):
#     print(i, end=" ")
# 8.
# n=int(input("N="))
# a=1
# for i in range(1,n):
#     a*=i
# print(a)

# 9.
# n=int(input("n="))
# sum=0
# for i in str(n):
#     sum+=int(i)
# print(sum)
# 10.
# n=int(input("N="))
# a=0
# for i in range(1,n):
#     a+=(i*i)
# print(a)
# 11.
# max = 0
# for i in range(10):
#     n = int(input(f"{i+1}-sonni kiriting: "))
#     if n >= max:
#         max=n
# print(max)
# 12.
# n=int(input("N= "))
# a=n
# for i in range(1,n+1):
#     if a%i==0:
#         print(i)
# 13.
# a="aueio"
# s=input("S=")
# sum=0
# for i in s:
#     if i.lower() in a:
#         sum+=1
# print(sum)
# 14.
# s=input("S= ")
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end="")
# 15.
# a=" "
# sum=0
# s=input("S= ")
# for i in str(s):
#     if i in a:
#         sum+=1
# print(sum)
# 16.
# n=int(input("a= "))
# for i in range(1,n):
#     if i%3==0 and i%5==0:
#         print(i,end=" ")
# 17.
# s=int(input("N= "))
# a=0
# for i in range(s):
#     n=int(input(f"{i+1}-son= "))
#     a+=i
# print(a/n)
# 18.
# a=input("S= ")
# lower=0
# upper=0
# for i in a:
#     if i.islower():
#         lower+=1
#     elif i.isupper():
#         upper+=1
# print("katta harflar soni ",upper)
# print("kichik harflar soni ",lower)
19.
# n=int(input("N="))
# i=2
# while i<=n:
#     j=2
#     while j<i:
#         if i%j==0:
#             break
#         j+=1
#     else:
#         print(j)
#     i+=1
# print()


