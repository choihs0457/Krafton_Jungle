import math

a = list(map(int,input().split()))
b =math.ceil((a[2]-a[0])/(a[0]-a[1]))+1
print(f'{b:.0f}')
    