# Recursion code

def f(i, j):
    '''
    calculates no of unique ways from (0,0) to (i,j)
    '''

    # Base condition
    if i == 0 and j == 0:
        return 1

    if i < 0 or j < 0:
        return 0
    
    # Do stuffs on (i,j)
    up = f(i-1, j)
    left = f(i, j - 1)

    return up + left

def f_memo(i, j, dp):

    if i == 0 and j == 0:
        return 1

    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]
    
    up = f_memo(i-1, j, dp)
    left = f_memo(i, j- 1, dp)

    dp[i][j] = up + left

    return dp[i][j]

def dpTable(m,n):

    dp = [[-1 for i in range(n)] for i in range(m)]

    #Initialisation
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                up = left = 0
                if i > 0:
                    up = dp[i-1][j]
                if j > 0:
                    left = dp[i][j-1]
                dp[i][j] = up + left
    
    return dp[m-1][n-1]


m = int(input("Enter m: "))
n = int(input("Enter n: ")) 
dp = [[-1 for _ in range(n)] for _ in range(m)]
print("Ans:", f_memo(m-1, n-1, dp))
print("Ans:", dpTable(m,n))