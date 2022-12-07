from sympy.ntheory import factorint
import math


def factors_int(num):
    poss_p = math.floor(math.sqrt(num))

    if poss_p % 2 == 0:
        poss_p += 1
    while poss_p < num:
        if num % poss_p == 0:
            return poss_p
        poss_p += 2


# n = 955933250882005692895759
# 24
n = int(input("Enter n: "))
print("Prime factors are: ", factorint(n))
