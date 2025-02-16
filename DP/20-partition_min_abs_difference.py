def minSubsetSumDifference(arr, n):

    totSum = sum(arr)

    dp = [[False for i in range(totSum + 1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = True

    if arr[0] <= totSum:
        dp[0][arr[0]] = True

    for ind in range(1, n):
        for target in range(1, totSum + 1):
            notTaken = dp[ind - 1][target]

            taken = False
            if arr[ind] <= target:
                taken = dp[ind - 1][target - arr[ind]]


            dp[ind][target] = notTaken or taken

    mini = int(1e9)

    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    return mini

arr = [1, 2, 3, 4]
n = len(arr)

print("Ans:", minSubsetSumDifference(arr, n))