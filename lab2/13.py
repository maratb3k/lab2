abc = list(input().split())

def funct():
    for i in range(len(abc)//2):
         if abc[i] != abc[len(abc)-i-1]:
            print("No")
            quit()
    print("Yes")

funct()