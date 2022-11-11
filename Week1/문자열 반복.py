a = int(input())
d = str()

for x in range(a):
    b = input().split()
    c = list(map(str, b[1]))
    for y in range(len(c)):
        d += (c[y]*int(b[0]))
    print(d)
    d = str()
