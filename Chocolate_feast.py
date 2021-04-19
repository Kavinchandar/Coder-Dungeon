t = int(input())
while t:
    n, c, m = map(int, input().split())
    total = wrappers = n//c
    while wrappers >= m:
        total += wrappers // m
        wrappers = wrappers // m + wrappers % m
    print(total)
    t -= 1
