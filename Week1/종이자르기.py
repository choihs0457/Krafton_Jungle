a, b = map(int, input().split())
c = int(input())
e = [a]
f = [b]
ee = []
ff = []
for x in range(c):
    d = list(map(int, input().split()))
    if d[0] != 0 :
        e.insert(len(e), int(d[1]))
    else:
        f.insert(len(f), int(d[1]))

for y in range(0, len(e)-1):
    e.sort()
    ee.insert(len(ee),e[y+1]-e[y])
for z in range(0, len(f)-1):
    f.sort()
    ff.insert(len(ff),f[z+1]-f[z])

ee.insert(len(ee),e[0])
ff.insert(len(ff),f[0])


print(max(ee)*max(ff))