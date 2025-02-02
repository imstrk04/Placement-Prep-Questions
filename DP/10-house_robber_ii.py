
def rob(nums):

    if len(nums) == 1:
        return nums[0]
    
    def helper(a):
        if not a:
            return 0

            
        n = len(a)

        prev2 = 0
        prev = a[0]

        for i in range(1, n):
            pick = a[i]
            if i > 1:
                pick += prev2
            notpick = prev

            curi = max(pick, notpick)

            prev2 = prev
            prev = curi
        
        return prev

    arr1, arr2 = [], []

    for i in range(len(nums)):
        if i != 0:
            arr1.append(nums[i])
        if i != len(nums) - 1:
            arr2.append(nums[i])
        
    ans1, ans2 = helper(arr1), helper(arr2)

    return max(ans1, ans2)