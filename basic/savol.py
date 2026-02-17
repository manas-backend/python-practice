

# 1-savol:  To‘rt sonning o‘rta arifmetigini toping.
sum=0
for i in range(4):
    a=int(input(f"{i} - sonni kiriting: "))
    sum+=i
print(sum/4)

# 2-savol: 3 xonali sonning eng kichik raqamini aniqlang. 
a=int(input("a = "))
s=a%100//10
d=a//100
f=a%10
if s<d and s<f or d==f:
    print("kivhik son ",s)
elif d<s and d<f or s==f:
    print("kichik son ",d)
else:
    print("kichik son ", f)

# 3-savol: Bahoga qarab so‘zli ta’rif chiqaring (“A’lo”, “Yaxshi”, “Qoniqarli”, “Yomon”).
a=int(input("Bahoni kiriting: "))
match a:
    case 0:print("Yomon")
    case 1:print("Yomon")
    case 2:print("Yomon")
    case 3:print("Qoniqarli")
    case 4:print("Yaxshi")
    case 5:print("A'lo")
    case _:print("Qanaqa baxo oldiz ozi !!!")

# 4-savol: 1 dan 1000 gacha bo‘lgan 12 ga bo‘linadigan sonlarni chiqaring.

for i in range(1,1001):
    if i%12==0:
        print(i, end=" ")


# 5-savol: Satrdagi kichik harflarni ekranga chiqaring.
a=input("Satrni kiriting: ")
for i in a:
    if i.islower():
        print(i, end=" ")


# 6-savol: Raqamlar soni harflardan kam bo‘lsa “ok”, aks holda “error”.
s=input("Satr kiriting: ")
harf = 0
raqam = 0
for i in s:
    if i.isalpha():
        harf += 1
    elif i.isdigit():
        raqam += 1
if raqam < harf:
    print("ok")
else:
    print("error")
