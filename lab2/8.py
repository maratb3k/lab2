k = list(input().split())
def minmax():
    b = -1000
    c = 1000
    for i in range(0,len(k)):
        if int(k[i]) > b:
            b = int(k[i])
        elif int(k[i]) < c:
            c = int(k[i])   
    print(c,b)

minmax()