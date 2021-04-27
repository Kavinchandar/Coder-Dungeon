n = int(input())
scores = list(map(int, input().split()))
most_count, least_count = 0, 0
maxx, minn = 0, 0
for i in range(n):
    temp = scores[:i+1]
    if i > 0:
        if scores[i] > maxx:
            most_count += 1
        elif scores[i] < minn:
            least_count += 1
    maxx = max(temp)
    minn = min(temp)

print(most_count, least_count)
