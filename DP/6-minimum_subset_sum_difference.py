def subsetSum(arr, sum):
    n = len(arr)
    t = [[False for _ in range(sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = True

    for i in range(1,n + 1):
        for j in range(1,sum + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]

            else:
                t[i][j] = t[i-1][j]

    return t[n][:(sum // 2) + 1]


def minSubsetSumDifference(arr, n):
    min_num = float('inf')

    total = sum(arr)

    num_list = subsetSum(arr, total)

    for idx, num in enumerate(num_list):
        if num:
            min_num = min(min_num, total - (idx*2))

    return min_num


arr = [1,5,6,11]
n = len(arr)
ans = minSubsetSumDifference(arr,n)
print("Ans:", ans)