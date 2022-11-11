a = int(input())

b = list(map(int, input().split()))
c = 0

for x in range(0, len(b)):
    if b[x] == 2:
        d = True
    elif b[x] == 1:
        d = False
    for y in range(2, b[x]):
        if b[x]%y == 0:
            d = False
            break
        else:
            d = True 
    if d == True:
        c += 1
        
print(c)