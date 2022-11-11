a = []
cnt = 0
for _ in range(0, 9):
    a.insert(len(a),int(input()))

for x in range(0, 9):
    if cnt == 1:
        break
    for y in range(1,9):
        if cnt == 1:
            break
        if a[x]+a[y] == sum(a)-100:
            a.remove(a[x])
            a.remove(a[y-1])
            print(*sorted(a), sep="\n")
            cnt = 1
            
