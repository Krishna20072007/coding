# import math
# import sys
# sys.set_int_max_str_digits(10000000)


# def prime(n):
#     return 1 + sum([
#         math.floor(pow(n/sum([
#             math.floor(pow(math.cos(math.pi*(math.factorial(j - 1) + 1) / j), 2))
#             for j in range(1, i+1)
#         ]), 1/n))
#         for i in range(1, pow(2, n) + 1)
#     ])

# for n in range(1, 9+1):
#     print(prime(n))




from math import cos, factorial, floor, pi


def X(i: int, n: int) -> int:
    y = Y(i, n)
    e = 1 / n
    r = pow(y, e)

    return floor(r)


def Y(i: int, n: int) -> float:
    def iterator(j: int) -> int:
        f = factorial(j - 1) + 1
        a = f / j
        b = a * pi
        c = cos(b)
        e = pow(c, 2)

        return floor(e)

    cs = [iterator(j) for j in range(1, i + 1)]

    return n / sum(cs)


def willans(n: int) -> int:
    xs = [X(i, n) for i in range(1, pow(2, n) + 1)]
    s = sum(xs)

    return 1 + floor(s)


lower_bound = 1
upper_bound = 5
result = [willans(n) for n in range(lower_bound, upper_bound + lower_bound)]

print(result)