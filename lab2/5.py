abc = list(input().split())
ind = int(input())
#b = len(abc)

def delet(abc):
    # for i in range(ind,b-1):
    #     del
    #     print (abc[i])
    del abc[ind:]
    print(abc)

delet(abc)