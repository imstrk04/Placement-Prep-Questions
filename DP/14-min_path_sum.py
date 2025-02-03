'''MICROSOFT QUESTION'''
## NOTE: Solved it without seeing Striver's solution
# recursion code

def f(i,j, a):
    up = left = 0

    if i < 0 or j < 0:
        return float('inf')
    
    if i == 0 and j == 0:
        return a[0][0]

    up = a[i][j] + f(i-1, j,a)
    left = a[i][j] + f(i, j -1,a)

    
    return min(up, left)


def f_memo(i,j,a, dp):
    up = left = 0

    if i < 0 or j < 0:
        return float('inf')
    
    if i == 0 and j == 0:
        return a[0][0]

    if dp[i][j] != -1: return dp[i][j]

    up = a[i][j] + f(i-1, j,a)
    left = a[i][j] + f(i, j -1,a)

    
    dp[i][j] = min(up, left)

    return dp[i][j]

a = [[5, 9, 6],[11,5, 2]]
n = len(a)
m = len(a[0])
dp = [[-1 for i in range(m)] for _ in range(n)]


def dpTable(a):

    n, m = len(a), len(a[0])

    dp = [[-1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = a[i][j]
            else:
                up = left = float('inf')
                if i > 0:
                    up = a[i][j] + dp[i-1][j]
                if j > 0:
                    left = a[i][j] + dp[i][j-1]

                dp[i][j] = min(up, left)

    return dp[n-1][m-1]

print("ans:", f(len(a)-1,len(a[0])-1, a))
print("ans:", f_memo(len(a)-1,len(a[0])-1, a,dp))
print("ans:", dpTable(a))
                    
