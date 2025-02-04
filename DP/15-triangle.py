# Recursion Code

def f(i,j, a):
    n = len(a)
    if i == n - 1:
        return a[i][j]
    
    down = a[i][j] + f(i+1, j,a)
    diagonal = a[i][j] + f(i+1, j + 1, a)

    return min(down, diagonal)

# Memoization
def f_memo(i, j, a, dp):
    n = len(a)
    if i == n - 1:
        return a[i][j]
    if dp[i][j] != -1: return dp[i][j]
    down = a[i][j] + f_memo(i+1, j,a,dp)
    diagonal = a[i][j] + f_memo(i+1, j + 1, a,dp)

    dp[i][j] = min(down, diagonal)
    
    return dp[i][j]

# Tabulation
def dpTable(a):

    n = len(a)

    dp = [[-1 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        dp[n-1][j] = a[n-1][j]

    for i in range(n-2, -1, -1):
        for j in range(i,-1,-1):
            down = a[i][j] + dp[i+1][j]
            diagonal = a[i][j] + dp[i+1][j+1]

            dp[i][j] = min(down, diagonal)
    
    return dp[0][0]

a = [
    [1],
    [2,3],
    [3,6,7],
    [8,9,6,10]
]
n = len(a)


dp = [[-1 for _ in range(n)] for _ in range(n)]
print("Ans:", f(0,0,a))
print("Ans:", f_memo(0,0,a,dp))
print("Ans:", dpTable(a))
