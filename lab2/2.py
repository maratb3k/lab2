l = list(input().split())

def funct(l):
    b = []
    for i in range(len(l)):
        if i%2==0:
            b.append(l[i])
    print(b)

funct(l)
