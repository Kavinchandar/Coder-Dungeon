b, w = map(int, input().split())
bc, wc, z = map(int, input().split())


def taumBday(b, w, bc, wc, z):
    # Write your code here
    base_cost = b*bc + w*wcs
    if bc > wc+z:
        base_cost = b*(wc+z) + w*wc
    elif wc > bc+z:
        base_cost = b*bc + w*(bc+z)
    elif bc == wc == z:
        pass
    return base_cost


print(taumBday(b, w, bc, wc, z))
