def isPrime(x):
    if x > 1:
        for i in range(2, x//2):
            #If num is divisible by any number between 2 and n/2, it is not prime
            if (x % i) == 0:
                return False
        else:
            return True
    else:
        return False

count = 0
n = 0
while count <= 10001:
    if isPrime(n):
        print("The", count, "prime is", n)
        count += 1
    n+=1
