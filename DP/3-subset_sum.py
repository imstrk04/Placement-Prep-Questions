# Subset Sum
'''
If sum is present in a subset, return True
'''
# Knapsack -> wt arr, val arr, W
# Subset Sum -> arr ~= wt arr and sum ~= W 


def subsetSum(arr, sum):
    n = len(arr)
    # Intialisation
    # Along Column => arr size, Along Row => Sum
    t = [[False for _ in range(sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = True

    # Knapsack Wt arr => arr []
    # Knapsack W => sum

    for i in range(1, len(arr) + 1):
        for j in range(1,sum + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]

            else:
                t[i][j] = t[i-1][j]

    
    print("ans:", t[len(arr)][sum])


arr = [2, 3, 7, 8, 10]
sum = 11


subsetSum(arr, sum)
