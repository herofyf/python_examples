import sys

'''
    当前的状态：idx最多下最多使用W重量，返回最大价值
'''
def knapsack_toptobottom(v, w, idx, W, mxTable):
    if idx < 0 or W <= 0:
        return 0
    if (w[idx] > W):
        return 0
    if mxTable[idx][W] > 0:
        return  mxTable[idx][W]
    mxTable[idx][W] = max(knapsack_toptobottom(v, w, idx - 1, W - w[idx], mxTable) + v[idx],
                        knapsack_toptobottom(v, w, idx - 1, W, mxTable))
    return mxTable[idx][W]

'''
返回的是最大值状态列表
'''
def knapsack_bottomtotop(v, w, n, limitW):
    # 当选了i物品, j重量时，最大价值值
    F = [ [0] * (limitW + 1) for i in range(n + 1) ]

    for i in range(0, n):
        for j in range(limit + 1):
            # i 表示选择第j个物品时，当前是重量j的最大值
            if w[i] <= j:
                # 第一种情况是不选当前的i,另一种情况是是选了
                F[i][j] = max(F[i -1][j], F[i-1][j - w[i]] + v[i])
            else:
                F[i][j] = F[i-1][j]
    return F

def showSelectItems(F, maxW, itemCount):
    y = maxW
    for i in range(itemCount - 1, -1, -1):
        if F[i][y] > F[i - 1][y]:
            print("item: ", i, "value:", v[i], "weight:", w[i])
            y -= w[i]

if __name__ == '__main__':
    #print(sys.argv)
    with open(sys.argv[1] if len(sys.argv) > 1 else sys.exit(1)) as f:
        #fist line includes max weight and the number of items
        limit, n = map(int, f.readline().split())
        v, w = zip(*[map(int, line.split()) for line in f.readlines()])
    F = knapsack_bottomtotop(v, w, n, limit)
    print('Max value: ', F[n -1][limit])
    showSelectItems(F, limit, n)
    F = [[0] * (limit + 1) for i in range(n + 1)]
    print('Max value:', knapsack_toptobottom(v, w, n - 1, limit,  F))
    showSelectItems(F, limit, n)


