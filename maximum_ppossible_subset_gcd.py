import itertools

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))


def find_gcd(x, y):
    if y == 0:
        return x
    else:
        return find_gcd(y, x % y)


def gcd(lst):
    num1 = lst[0]
    num2 = lst[1]
    gcd = find_gcd(num1, num2)
    for i in range(2, len(lst)):
        gcd = find_gcd(gcd, lst[i])
    return gcd


def findsubsets(s, n):
    return list(itertools.combinations(s, n))


def subsets(lst):
    n = len(lst)
    subset = {}
    while n > 1:
        try:
            subset[n].append(findsubsets(lst, n))
        except KeyError:
            subset[n] = findsubsets(lst, n)
        n -= 1
    return subset


def max_possible_gcd(lst):
    m = 0
    test = subsets(lst)
    for i in test:
        if i >= 2:
            for j in test[i]:
                m = max(m, gcd(j))
    return m


print(subsets(lst))
print(max_possible_gcd(lst))
