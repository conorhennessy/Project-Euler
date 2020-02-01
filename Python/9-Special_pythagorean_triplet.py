import math
import sys

sum = 1000
for a in range(3, int((sum-3)/3)):
    for b in range(a + 1, int((sum-1-a)/2)):
        if math.sqrt(a ** 2 + b ** 2).is_integer():
            c = math.sqrt(a ** 2 + b ** 2)
            if a+b+c == 1000:
                print(a,b,c)
                print(a*b*c)
                sys.exit()


# sum = 1000
# for a in range(3, int((sum-3)/3)):
#     for b in range( a + 1, int((sum-1-a)/2)):
#         c = sum - a - b
#         if a ** 2 + b ** 2 == c ** 2:
#             if a+b+c == 1000:
#                 print(a,b,c)
#                 print(a*b*c)
#                 sys.exit()