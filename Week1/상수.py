a, b = map(list, input().split())
c = []
d = []
for x in range(len(a)-1, -1, -1):
    c.insert(len(c), a[x])
    d.insert(len(d), b[x])
if "".join(c) >"".join(d):
    print("".join(c))
else:
    print("".join(d))
