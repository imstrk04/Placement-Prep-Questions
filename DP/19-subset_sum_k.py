# Recursion Code

# f(x, target) -> means till xth index, target can be found?

# TC: O(2^n), SC: O(N)

def f(a,ind, target):
    
    if target == 0:
        return True
    
    if ind == 0:
        return a[0] == target
    
    notpick = f(a, ind - 1, target)
    pick = False

    if target >= a[ind]:
        pick = f(a, ind - 1, target - a[ind])
    
    return pick or notpick # if anything give me true or false, i will take

# Memoization
def f_memo(a,ind, target, dp):
    
    if target == 0:
        return True
    
    if ind == 0:
        return a[0] == target
    
    if dp[ind][target] != -1:
        return dp[ind][target]

    notpick = f(a, ind - 1, target)
    pick = False

    if target >= a[ind]:
        pick = f(a, ind - 1, target - a[ind])
    
    dp[ind][target] = pick or notpick # if anything give me true or false, i will take

    return dp[ind][target]

def dpTable(a, target):
    n = len(a)

    dp = [[False for _ in range(target + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    if a[0] <= target:
        dp[0][a[0]] = True

    for i in range(1,n):
        for j in range(1,target+1):
            notpick = dp[i-1][j]
            pick = False
            if a[i] <= target:
                pick = dp[i-1][j-a[i]]
            
            dp[i][j] = pick or notpick

    return dp[n-1][target]

a = [1,2,3,4]
target = 4

n = len(a)
print("Ans:", f(a,n-1, target))

dp = [[-1 for _ in range(target+1)] for _ in range(n)]
print("Ans:", f_memo(a, n - 1, target, dp))
print("Ans:", dpTable(a, target))