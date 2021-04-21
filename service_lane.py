n, t = map(int, input().split())
widths = list(map(int, input().split()))
cases = []
while t:
    x = list(map(int, input().split()))
    cases.append(x)
    t -= 1
for i in cases:
    print(min(widths[i[0]:i[-1]+1]))
