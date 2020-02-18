a = float(input())
n = int(input())

def p(a, n):
    r = 1
    for i in range(abs(n)):
        r *= a
    if n >= 0:
        return r
    else:
        return 1 / r

print(p(a,n))
