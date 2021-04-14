import sys
n = int(input())
a = list(map(int, input().split()))
d = {}
dist = sys.maxsize
for i in range(n):
    try:
        d[a[i]].append(i)
    except KeyError:
        d[a[i]] = [i]


for i in d:
    if len(d[i]) == 2:
        dist = min(dist, abs(d[i][1]-d[i][0]))

for i in d:
    if len(d[i]) == 2:
        break
else:
    dist = -1

print(dist)
