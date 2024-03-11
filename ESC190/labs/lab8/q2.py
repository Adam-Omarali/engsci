import numpy as np

def make_change(coins, amt):
    OPT = [np.inf] * (amt + 1)
    #OPT[v] = min(1 + OPT[v - c] for c in coins)
    OPT[0] = 0

    for v in range(1, amt + 1):
        for c in coins:
            if v - c >= 0:
                OPT[v] = min(1 + OPT[v - c], OPT[v])

    s = 0
    count = 0
    coins_used = []
    while s != amt:
        min_coin = 0
        min_OPT = np.inf
        for c in coins:
            if s + c <= amt:
                if OPT[amt - s - c] < min_OPT:
                    min_OPT = OPT[amt - s - c]
                    min_coin = c
        s += min_coin
        count += 1
        coins_used.append(min_coin)

    print("minimum coins: ", count, " | coins used: ", coins_used)


make_change([1, 3, 4], 9)