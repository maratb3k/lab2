a = set(input().split())
b = set(input().split())
 
def diff(a,b):
    return a.difference(b)

print(diff(a,b))