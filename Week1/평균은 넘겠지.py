a = int(input())
d = 0

for x in range(a):
    b = list(map(int, input().split()))
    c = int((sum(b)-b[0])/b[0])
    for y in range(1, len(b)):
        if b[y] > c:
            d += 1
    print(f'{round(d/b[0]*100, 3):.3f}%')
    c = 0
    d = 0