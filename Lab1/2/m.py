a = int(input())
c = int(input())
b = int(input())
rem1 = 0
rem2 = 0
rem3 = 0
if a%2!=0 or b%2!=0 or c%2!=0:
    rem1 = a%2 
    rem2 = b%2
    rem3 = c%2
a1 = (a//2)+rem1
b1 = (b//2)+rem2 
c1 = (c//2)+rem3  
print(a1+b1+c1)