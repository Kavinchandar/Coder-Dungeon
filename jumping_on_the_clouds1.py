n, k = map(int, input().split())
c = list(map(int, input().split()))
i = k % n
count = c[i]*2 + 1
while i != 0:
    i = (i+k) % n
    count += c[i]*2 + 1

print(100-count)
