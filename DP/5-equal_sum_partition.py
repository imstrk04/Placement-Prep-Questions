
def canPartition(nums):
    
    def subsetSum(arr, sum):
        n = len(arr)
        t = [[False for _ in range(sum + 1)] for _ in range(n+1)]

        for i in range(n+1):
            t[i][0] = True
        
        for i in range(n+1):
            for j in range(sum + 1):
                if i == 0:
                    t[i][j] = False
                if j == 0:
                    t[i][j] = True
        
        for i in range(1,n + 1):
            for j in range(1, sum + 1):
                if arr[i-1] <= j:
                    t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        
        return t[n][sum]
    
    sum_of_nums = sum(nums)
    if sum_of_nums % 2 != 0:
        return False
    else:
        return subsetSum(nums, sum_of_nums // 2)