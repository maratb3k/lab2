abc = list(input().split())
b = int(input())

def funct():
    for i in range(len(abc)):
        if int(abc[i]) > b:
            print(int(abc[i]))

funct()