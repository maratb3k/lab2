a = str(input())
b = len(a)
k = ""
s = ""
q = ""
r = ""
print(a[2])
print(a[b-2])
print(a[:5])
print(a[:-2])
for i in range (0,b):
    if i%2==0:
        s += a[i]
print(s)
for i in range(1,len(a)):
    if i%2!=0:
        k += a[i]
print(k)
for i in range(len(a)-1, -1, -1):
    q+=a[i]
print(q)
for i in range(len(a)-1, -1,-2):
    r += a[i] 
print(r)
print(b)