a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)
e = list(map(int, d))

for x in range(0, 10):
    f = 0
    for y in range(len(e)):
        if e[y] == x:
            f += 1
    print(f)