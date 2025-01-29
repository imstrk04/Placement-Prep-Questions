# Knapsack - Top Down
n = 4
W = 7  # Knapsack capacity

wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]

t = [[-1 for _ in range(W+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(W+1):
        if i == 0 or j == 0:
            t[i][j] = 0

for i in range(n+1):
    for j in range(W+1):
        if wt[i-1] <= j:
            t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])

        else:
            t[i][j] = t[i-1][j]

print("ans:", t[n][W])