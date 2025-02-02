arr = [30, 10, 60, 10, 60, 50]
n = 6

# Recursion code

def f(index, heights):

    if index == 0:
        return 0

    left = f(index - 1, heights) + abs(heights[index] - heights[index - 1])
    right = float('inf') # Because this is not gonna happen always

    if index > 1:
        right = f(index - 2, heights) + abs(heights[index] - heights[index - 2])

    return min(left, right)

def frogJumpRecurr(n, heights):

    return f(n - 1, heights)


def f_memo(index, heights, dp):
    if index == 0:
        return 0

    if dp[index] != -1:
        return dp[index]

    left = f_memo(index - 1, heights, dp) + abs(heights[index] - heights[index - 1])
    right = float('inf')  # Right step won't always happen

    if index > 1:
        right = f_memo(index - 2, heights, dp) + abs(heights[index] - heights[index - 2])

    dp[index] = min(left, right)
    return dp[index]  # Return the result after calculating it

def frogJumpMemo(n, heights):
    dp = [-1] * (n + 1)  # Create dp array to store results
    return f_memo(n - 1, heights, dp)  # Call for the last index (n-1) not n

def frogJumpDP(n, heights):

    t = [0] * (n)

    t[0] = 0

    for i in range(1, n):
        first_step = t[i - 1] + abs(heights[i - 1] - heights[i])
        second_step = float('inf')
        if i > 1:
            second_step = t[i - 2] + abs(heights[i-2] - heights[i])

        t[i] = min(first_step, second_step)
    
    return t[n-1]

print(frogJumpRecurr(n, arr))
print(frogJumpMemo(n, arr))
print(frogJumpDP(n, arr))