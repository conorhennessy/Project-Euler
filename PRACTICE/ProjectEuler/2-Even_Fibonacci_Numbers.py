import math
from functools import lru_cache

@lru_cache(3)

def fibonacci(n):
    """" Finds fibonacci number for index supplied
    Recursive function to find the fibonacci number for a certain index
    where F{n} = F{n-1} + F{n-2}.
    This function utilises lru_cache to cache recently computed results
    in order for faster calculations at the next iteration.

    Args:
        n, the current index to be found.
    Returns:
       The fibonacci number for this index.
    """

    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

f = 1
sum = 0
while fibonacci(f) < 4000000:
    if fibonacci(f) % 2 == 0:
        sum += fibonacci(f)
    f+=1

print("Answer: ", sum)