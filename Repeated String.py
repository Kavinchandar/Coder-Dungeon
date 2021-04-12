s = input()
n = int(input())
l = len(s)
t = s.count('a')
if n <= l:
    s = s[:n]
    print(s.count('a'))
else:
    count = n//l
    remainder = n % l
    s = s[:remainder]
    print((count*t)+(s.count('a')))
