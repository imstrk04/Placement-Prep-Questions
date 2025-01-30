arr = [2,3,5,6,8,10]
sum = 10
n = len(arr)

def count_subsets(arr, sum, n):

    t = [[0 for _ in range(sum + 1)] for _ in range(n+1)]

    for i in range(n + 1):
        t[i][0] = 1
    
    for i in range(1,n + 1):
        for j in range(1,sum + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    print("count:", t[n][sum])

count_subsets(arr, sum, n)