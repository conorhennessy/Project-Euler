n = 1
i = 1

while i <= 20:
    if n % i != 0:
        n += 1
        i = 0
    if i == 20:
        print(n)
    i += 1

#My solution is incredibly slow, avg of 272s (4min32sec) to solve