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

# As we know that 2 is our first prime
count = 2
n = 1
while count <= 10001:
    # Addition of two as we know all primes except tow are odd.
    # So no need to iterate up by one each time.
    n+=2
    if isPrime(n):
        print("The", count, "prime is", n)
        count += 1

