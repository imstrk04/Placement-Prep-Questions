# Recursion code

def f(i, j1, j2,n, m, a):

    if j1 < 0 or j2 < 0 or j1 >= m or j2 >= m:
        return -1e9

    if i == n - 1:
        if j1 == j2:
            return a[i][j1]
        else:
            return a[i][j1] + a[i][j2]

    # explore all paths of Alice and Bob
    maxi = float('-inf')
    for dj1 in range(-1, 2):
        for dj2 in range(-1, 2):
            value = 0
            if j1 == j2:
                value = a[i][j1]
            else:
                value = a[i][j1] + a[i][j2]
            
            value += f(i+1, j1 + dj1, j2 + dj2, n, m, a)

            maxi = max(maxi, value)

    return maxi

# Memoization
def f_memo(i, j1, j2, n, m, a, dp):

    if j1 < 0 or j2 < 0 or j1 >= m or j2 >= m:
        return -1e9

    if i == n - 1:
        if j1 == j2:
            return a[i][j1]
        else:
            return a[i][j1] + a[i][j2]
    
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2 ]

    # explore all paths of Alice and Bob
    maxi = float('-inf')
    for dj1 in range(-1, 2):
        for dj2 in range(-1, 2):
            value = 0
            if j1 == j2:
                value = a[i][j1]
            else:
                value = a[i][j1] + a[i][j2]
            
            value += f_memo(i+1, j1 + dj1, j2 + dj2, n, m, a,dp)

            maxi = max(maxi, value)
    
    dp[i][j1][j2] = maxi

    return dp[i][j1][j2]




a = [
    [2,3,1,2],
    [3,4,2,2],
    [5,6,3,5]
]
n, m = len(a), len(a[0])
dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]

print("Ans:", f(0,0,m-1,n, m, a))
print("Ans:", f_memo(0,0,m-1,n, m, a, dp))