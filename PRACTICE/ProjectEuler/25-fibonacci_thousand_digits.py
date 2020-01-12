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

n = 0  # Representing current index in sequence
digits = 1  # Count number of digits in current value

while digits < 1000:
    n+=1
    digits = int(math.log10(fibonacci(n)) + 1)
    fibonacci(n)

print("Result:\nThe first number in the Fibonacci sequence with", digits, "digits (at index", n, "in the sequence) is... \n")
print(fibonacci(n))
