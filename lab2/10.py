abc  = set(input().split())

def funct():
    b = set()
    for i in abc:
        b.add(int(i)-1)
        b.add(int(i)+1)
    print(b)
    
funct()