# Recursion

def f(ind, a):

    if ind == 0:
        return a[ind]
    
    if ind < 0:
        return 0

    pick = a[ind] + f(ind - 2,a)
    notpick = 0 + f(ind - 1,a)

    return max(pick, notpick)

# Memoization

def f_memo(ind, a,dp):

    if ind == 0:
        return a[ind]
    
    if ind < 0:
        return 0

    if dp[ind] != -1:
        return dp[ind]
    

    pick = a[ind] + f_memo(ind - 2,a, dp)
    notpick = 0 + f_memo(ind - 1,a, dp)

    dp[ind] = max(pick, notpick)
    return dp[ind]

def memo(ind, nums):
    n = len(nums)

    dp = [-1] * n

    return f_memo(n-1, nums, dp)

def dpSoln(a):
    n = len(a)

    dp = [-1] * n

    dp[0] = a[0]

    for i in range(1, n):

        pick = a[i]
        if i > 1:
            pick += dp[i-2]
        notpick = dp[i-1]

        dp[i] = max(pick, notpick)
    
    return dp[n-1]

# Space Optimisation
def spaceOpt(a):
    n = len(a)

    prev = a[0]
    prev2 = 0

    for i in range(1, n):
        pick = a[i]
        if i > 1:
            pick += prev2
        
        notpick = prev

        curi = max(pick, notpick)

        prev2 = prev
        prev = curi
    
    return prev



a = [2,1,4,9]
ans = f(3, a)
ans2 = memo(3, a)
ans3 = dpSoln(a)
ans4 = spaceOpt(a)
print(ans)
print(ans2)
print(ans3)
print(ans4)