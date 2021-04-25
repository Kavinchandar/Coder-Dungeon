n, k = map(int, input().split())
s = list(map(int, input().split()))
ans = [0]*k
for i in s:
    ans[i % k] += 1
print(ans)
count = min(ans[0], 1)
for i in range(1, k//2+1):
    if i != k-i:
        count += max(ans[i], ans[k-i])
if k % 2 == 0:
    count += 1
print(count)
