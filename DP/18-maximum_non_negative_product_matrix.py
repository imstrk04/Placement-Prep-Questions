def f(i, j, grid):

    if i == 0 and j == 0:
        return (grid[i][j], grid[i][j]) 
    
    maxVal, minVal = float('-inf'), float('inf')

    if i > 0:
        upMax, upMin = f(i - 1, j, grid)
        maxVal = max(maxVal, upMax * grid[i][j], upMin * grid[i][j])
        minVal = min(minVal, upMax * grid[i][j], upMin * grid[i][j])
    
    
    if j > 0:
        leftMax, leftMin = f(i, j -1, grid)
        maxVal = max(maxVal, leftMax * grid[i][j], leftMin * grid[i][j])
        minVal = min(minVal, leftMax * grid[i][j], leftMin * grid[i][j])

    return maxVal, minVal

def f_memo(i,j, grid, dp):

    if i == 0 and j == 0:
        return (grid[i][j], grid[i][j]) 
    
    maxVal, minVal = float('-inf'), float('inf')

    if dp[i][j] != -1:
        return dp[i][j]

    if i > 0:
        upMax, upMin = f_memo(i - 1, j, grid,dp)
        maxVal = max(maxVal, upMax * grid[i][j], upMin * grid[i][j])
        minVal = min(minVal, upMax * grid[i][j], upMin * grid[i][j])
    
    
    if j > 0:
        leftMax, leftMin = f_memo(i, j -1, grid,dp)
        maxVal = max(maxVal, leftMax * grid[i][j], leftMin * grid[i][j])
        minVal = min(minVal, leftMax * grid[i][j], leftMin * grid[i][j])

    dp[i][j] = (maxVal, minVal)

    return dp[i][j]

def dpTable(grid):

    MOD = 10 ** 9 + 7

    n,m = len(grid), len(grid[0])

    dp = [[[0,0] for _ in range(m)] for _ in range(n)]

    dp[0][0] = [grid[0][0], grid[0][0]]

    # filling first row
    for j in range(1,n):
        dp[0][j][0] = dp[0][j-1][0] * grid[0][j]
        dp[0][j][1] = dp[0][j-1][1] * grid[0][j]    

    # filling first col
    for i in range(1,m):
        dp[i][0][0] = dp[i-1][0][0] * grid[i][0]
        dp[i][0][1] = dp[i-1][0][1] * grid[i][0]    

    for i in range(1, m):
        for j in range(1,n):
            upMax = dp[i-1][j][0]
            upMin = dp[i-1][j][1]

            leftMax = dp[i][j-1][0]
            leftMin = dp[i][j-1][1]

            dp[i][j][0] = max(upMax * grid[i][j], upMin * grid[i][j], leftMax * grid[i][j], leftMin * grid[i][j] )
            dp[i][j][1] = min(upMax * grid[i][j], upMin * grid[i][j], leftMax * grid[i][j], leftMin * grid[i][j] )

    maxProd, minProd = dp[m-1][n-1]

    return -1 if maxProd < 0 else maxProd % MOD



grid = [[1,-2,1],[1,-2,1],[3,-4,1]]

n, m = len(grid), len(grid[0])

dp = [[-1 for _ in range(m)] for _ in range(n)]
ans, _ = f(n-1, m - 1, grid)

memo_ans, _ = f_memo(n-1, m - 1, grid, dp)

print("Ans:", ans)
print("Ans:", memo_ans)
print("Ans:", dpTable(grid))