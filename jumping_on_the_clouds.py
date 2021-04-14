n = int(input())
a = list(map(int, input().split()))
count = 0
i = 0
while i <= n-2:
    if a[i] == 0:
        if i+2 < n and a[i+2] == 0:
            count += 1
            i += 2
        elif a[i+1] == 0:
            count += 1
            i += 1
        else:
            i += 3
    elif a[i] == 1:
        i += 1

print(count)
