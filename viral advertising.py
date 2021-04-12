

n = int(input())


def advert(n):
    like = 0
    temp = 5
    ans = []
    for _ in range(n):
        like = temp//2
        ans.append(like)
        temp = like * 3
    return sum(ans)


print(advert(n))
