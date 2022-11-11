a = int(input())
b = []
for x in range(a):
    b.insert(len(b), int(input()))
    b.sort()

print(*b, sep='\n')