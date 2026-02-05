#Variant 1 
# Eng oson usul: stringni teskarisiga solishtirish
def isPalindrome_v1(x: int) -> bool:
    return str(x) == str(x)[::-1]


# Variant 2
# reversed() funksiyasi bilan
def isPalindrome_v2(x: int) -> bool:
    s = str(x)
    return s == "".join(reversed(s))


# Variant 3
# Matematik usul (string ishlatmasdan)
def isPalindrome_v3(x: int) -> bool:
    if x < 0:
        return False
    
    original = x
    rev = 0
    
    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10
    
    return original == rev


# ================= Test =================
if __name__ == "__main__":
    test_numbers = [121, -121, 10, 1221, 12321]
    
    for n in test_numbers:
        print(f"{n} -> V1: {isPalindrome_v1(n)}, V2: {isPalindrome_v2(n)}, V3: {isPalindrome_v3(n)}")
