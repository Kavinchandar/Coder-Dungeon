p, d, m, s = map(int, input().split())
ans = []
sum = 0
count = 0
while p >= m:
    ans.append(p)
    p = p-d
for i in ans:
    sum += i
    if sum >= s:
        break
while s > sum:
    ans.append(m)
    sum += m

temp = 0
for i in ans:
    if temp+i > s:
        break
    temp += i
    count += 1
print(count)
