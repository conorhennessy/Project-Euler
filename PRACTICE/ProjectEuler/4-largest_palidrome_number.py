import math

def isPalindrome(x: int) -> bool:
    if x == 0:
        return True

    digits = int(math.log10(abs(x)) + 1)
    reverse = ""
    num = str(x)
    while digits > 0:
        reverse += num[digits - 1]
        digits -= 1

    return reverse == num

largest = 0
a = 999
while a >= 100:
    b = 999
    while b >= a:
        if a*b <= largest:
            break
        if isPalindrome(a * b):
            largest = a * b
        b -= 1
    a -= 1

print("Largest palindrome:",largest)
