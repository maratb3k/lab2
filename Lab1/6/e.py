s = input()
cnt = len(s) - len(s.replace('f', ''))
if cnt == 0:
    pass
elif cnt == 1:
    print(s.index('f'))
else: 
    print(s.index('f'), s.rindex('f'))