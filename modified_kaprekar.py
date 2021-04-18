p = int(input())
q = int(input())
ans = []
for i in range(p, q+1):
    temp = str(i**2)
    d = len(temp)
    left = temp[:d//2].strip(" ")
    right = temp[d//2:].strip(" ")
    if i == 1:
        ans.append(i)
    elif i >= 4:
        sum = int(left)+int(right)
        if sum == i:
            ans.append(i)
    else:
        pass

if ans == []:
    print('INVALID RANGE')
else:
    for i in ans:
        print(i, end=" ")
