limit = 100
sumSquares = 0
sum = limit * (limit+1) /2
i = 0
while i <= limit:
    sumSquares += pow(i, 2)
    i += 1

print("Difference:", pow(sum, 2) - sumSquares)
