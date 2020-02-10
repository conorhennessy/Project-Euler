# Version one - incredibly slow, so needed to optimise
# def isPrime(x):
#     if x > 1:
#         for i in range(2, x//2):
#             #If num is divisible by any number between 2 and n/2, it is not prime
#             if (x % i) == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# sum = 0
# for i in range(0, 2000000):
#     if isPrime(i):
#         sum += i
#
# print(sum)

# Version two - learning and implementation of eratosthenes sieve, however not ideal for such a large number
# def sum_sieve_of_eratosthenes(n):
#     sum = 0
#
#     #Create a list of consecutive integers, where this list is a boolean list
#     # so allows us to understand if a certain number (index) is prime, if false it is composite
#     is_prime =  [True]*(n-1)
#
#     p = 2 #Stores current prime
#
#     #itterate through all multiples of p, to change value & signify that they are composite
#     while True:
#         multiplier = 2
#         multiple = p * multiplier # (2p, 3p, 4p, ...)
#         while multiple <= n:
#             is_prime[multiple - 2] = False # -2 for the mapping of integer number to index location of boolean flag
#             multiplier += 1
#             multiple = p * multiplier
#
#         #Find new p value as this current prime value is complete
#         for i,prime in enumerate(is_prime):
#             if prime and i+2 > p:
#                 p = i + 2
#                 break # next prime has been found
#         else:
#             break # Reached end of algorithm so break out
#
#     for i,prime in enumerate(is_prime):
#         if prime:
#             sum += i+2
#
#     return sum
#
# print(sum_sieve_of_eratosthenes(2000000))

# Version three - this is version 2 of my eratosthenes implementation!
def eratosthenes2(n):
    #Declare a set - an unordered collection of unique elements
    multiples = set()

    #Iterate through [2,2000000]
    for i in range(2, n+1):
        #If i has not been eliminated already
        if i not in multiples:
            #Yay prime! So yield i, to be added ot the list
            yield i
            #Add multiples of the prime in the range to the 'invalid' set
            multiples.update(range(i*i, n+1, i))

#Now find the sum
sum = 0
primes_to_limit = list(eratosthenes2(2000000))
for x in primes_to_limit:
    sum = int(x) + sum

print(sum)