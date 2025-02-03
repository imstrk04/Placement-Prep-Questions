# Recursion code:

def f(day, last, points):

    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])

        return maxi

    maxi = 0

    for task in range(3):
        if task != last:
            point = points[day][task] + f(day - 1, task, points)
            maxi = max(maxi, point)
        
    return maxi

def ninjaTraining(n, points):

    return f(n-1, 3, points)


# Memoization

def f_memo(day, last, points, dp):

    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])

        return maxi

    if dp[day][last] != -1 :
        return dp[day][last]

    maxi = 0

    for task in range(3):
        if task != last:
            point = points[day][task] + f(day - 1, task, points)
            maxi = max(maxi, point)
        
    dp[day][last] = maxi

    return dp[day][last]

def ninjaTrainingMemo(n, points):

    dp = [[-1 for i in range(4)] for i in range(n)]

    return f_memo(n-1, 3, points, dp)

    # TC: O(N), SC: O(N) + O(Nx4)

def ninjaTrainingDPTable(n, points):

    dp = [[-1 for i in range(4)] for i in range(n)]

    # Initialisation
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][1], points[0][0])
    dp[0][3] = max(points[0][0],points[0][1], points[0][2])

    # Solving
    for day in range(1, n):
        for last in range(4):
            for task in range(3):
                if task != last:
                    point = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last], point)
    
    return dp[n-1][3]

    # TC: O(Nx4x3), SC: O(Nx4)

def ninjaTrainingSpaceOptimised(n, points):
    # go to striver video at time 46:30, he will explain why we need just the prev row in the table and not the full table, so each time lets just have an array of size 4 and keep overwriting on it

    prev = [0] * 4
    # Initialisation
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][1], points[0][0])
    prev[3] = max(points[0][0],points[0][1], points[0][2])

    for day in range(1, n):
        temp = [0] * 4
        for last in range(4):
            
            for task in range(3):
                if task != last:
                    point = points[day][task] + prev[task]
                    temp[last] = max(temp[last], point)
        prev = temp

    return prev[3] 

points = [
    [10, 11, 19],
    [4, 13, 7],
    [1, 8, 13]
]
n = 3

print("Ans:", ninjaTraining(n, points))
print("Ans:", ninjaTrainingMemo(n, points))
print("Ans:", ninjaTrainingDPTable(n, points))
print("Ans:", ninjaTrainingSpaceOptimised(n, points))