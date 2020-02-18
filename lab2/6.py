mylist = list(input().split())
ind1 = int(input())
mylist2 = list(input().split())

def funct():
    mylist.insert(ind1,mylist2)
    ind2 = int(input())
    del mylist[ind2:]
    print(mylist)

funct()