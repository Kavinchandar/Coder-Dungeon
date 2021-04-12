string = input()
n = len(string)
st = ""
lst, ans = [], []
lst.append(string[0])
for i in range(1, n):
    if string[i] == string[i-1]:
        pass
    else:
        lst.append(string[i])

for i in lst:
    st += i
j = 0
for i in st:
    count = 0
    while j != n and string[j] == i:
        count += 1
        j += 1
    ans.append((count, int(i)))

for i in ans:
    print(i, end=" ")
