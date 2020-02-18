p = int(input())
x = int(input())
y = int(input())
year = int(input())
a = (x*100)+y
k = (a*(p+100)/100)*5
first = int(k//100)
second = int(k%100)
print(first,second)