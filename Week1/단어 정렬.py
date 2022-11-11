a = int(input())
c = []
for b in range(a):
    d = input()
    if d in c:
        c.remove(d)
    c.insert(len(c),d)

c.sort()
c.sort(key=len)
print(*c, sep="\n")