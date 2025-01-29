# Memoization - Knapsack
n = 4
W = 7  # Knapsack capacity

wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]


t = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

def knapsack(wt, val, W, n):
    
    # Base Condition
    if W == 0 or n == 0:
        return 0

    if t[n][W] != -1:
        return t[n][W]

    # Choice Diagram
    if wt[n - 1] <= W:
        t[n][W] = max(
            val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1),
            knapsack(wt, val, W, n - 1)
        )
    else:
        t[n][W] = knapsack(wt, val, W, n - 1)

    return t[n][W]

print("ans:", knapsack(wt, val, W, n))
