abc = list(input().split())

def funct():
    cnt = 0
    for i in range(len(abc)):
        if i%2==0:
            if int(abc[i])%2!=0:
                cnt = i
                print(cnt)        
funct()