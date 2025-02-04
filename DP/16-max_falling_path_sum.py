# Start anywhere from first row and end anywhere in the last row

# Recursion

def f(i,j,a):
    '''
    maximum path sum to reach (i,j) from any cell in the first row.
    '''
    n, m = len(a), len(a[0])

    #out of bound case
    if j < 0 or j >= m:
        return float('-inf')
    
    if i == 0:
        return a[0][j]
    
    up = a[i][j] + f(i-1,j,a)
    left_diagonal = a[i][j] + f(i-1, j-1,a)
    right_diagonal = a[i][j] + f(i-1, j+1,a)

    return max(up, max(left_diagonal, right_diagonal))

def f_memo(i, j, a, dp):
    n, m = len(a), len(a[0])

    #out of bound case
    if j < 0 or j >= m:
        return float('-inf')
    
    if i == 0:
        return a[0][j]

    if dp[i][j] != -1: return dp[i][j]
    
    up = a[i][j] + f_memo(i-1,j,a,dp)
    left_diagonal = a[i][j] + f_memo(i-1, j-1,a,dp)
    right_diagonal = a[i][j] + f_memo(i-1, j+1,a,dp)

    dp[i][j] =  max(up, max(left_diagonal, right_diagonal))

    return dp[i][j]

def dpTable(a):
    n, m = len(a), len(a[0])

    dp = [[0 for j in range(m)] for i in range(n)]

    for j in range(m):
        dp[0][j] = a[0][j]

    for i in range(1,n):
        for j in range(m):
            up = a[i][j] + dp[i-1][j]

            left_diagonal = a[i][j]

            if j - 1 >= 0:
                left_diagonal += dp[i-1][j-1]
            else:
                left_diagonal += -int(1e9)
            
            right_diagonal = a[i][j]

            if j + 1 < m:
                right_diagonal += dp[i-1][j+1]
            
            else:
                right_diagonal += -int(1e9)
    
            dp[i][j] = max(up, left_diagonal, right_diagonal)
    
    maxi = float('-inf')

    for j in range(m):
        maxi = max(maxi, dp[n-1][j])
    
    return maxi

a = [
    [1,2,10,4],
    [100,3,2,1],
    [1,1,20,2],
    [1,2,2,1]
]
n = len(a)
m = len(a[0])
max_sum = max(f(n-1, j, a) for j in range(m))
dp = [[-1 for j in range(m)] for i in range(n)]
print("Ans:", max_sum)
maxi = float('-inf')

for j in range(m):
    ans = f_memo(n-1, j,a, dp)
    maxi = max(maxi, ans)

print("Ans:", maxi)

print("Ans:",dpTable(a))