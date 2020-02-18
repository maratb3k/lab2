l = list(int((input().split())))
ind = int(input())

def  funct():
    for i in range(ind,len(l)):            
            l[i]=int(l[i])**2
    print(l)

funct()