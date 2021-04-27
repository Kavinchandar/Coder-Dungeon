def ifeven(B):
    for i in B:
        if i % 2 != 0:
            return False
    return True


n = int(input())
B = list(map(int, input().split()))
count = 0
for i in range(n-1):
    if B[i] % 2 != 0:
        count += 2
        B[i] += 1
        B[i+1] += 1

if ifeven(B):
    print(count)
else:
    print('NO')
