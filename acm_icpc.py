from itertools import combinations
n, m = map(int, input().split())
teams = [list(map(int, input())) for i in range(n)]
print(teams)
maxx = [sum([x[0] or x[1] for x in list(zip(*i))])
        for i in combinations(teams, 2)]
print(max(maxx), maxx.count(max(maxx)), sep='\n')
