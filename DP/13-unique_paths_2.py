def f(i, j, a):
    '''
    calculates no of unique ways from (0,0) to (i,j)
    '''
    if i >= 0 and j >= 0 and a[i][j] == -1: # Extra base case to handle the dead cell in the matrix via which u cant travel to destination cell
        return 0
    # Base condition
    if i == 0 and j == 0:
        return 1

    if i < 0 or j < 0:
        return 0
    
    # Do stuffs on (i,j)
    up = f(i-1, j,a)
    left = f(i, j - 1,a)
    return up + left

def f_memo(i, j, a, dp):
    '''
    calculates no of unique ways from (0,0) to (i,j)
    '''
    if i >= 0 and j >= 0 and a[i][j] == -1: # Extra base case to handle the dead cell in the matrix via which u cant travel to destination cell
        return 0
    # Base condition
    if i == 0 and j == 0:
        return 1

    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    # Do stuffs on (i,j)
    up = f_memo(i-1, j,a,dp)
    left = f_memo(i, j - 1,a,dp)

    dp[i][j] = up + left

    return dp[i][j]


def mazeObstaclesUtil(n, m, maze, dp):
    # Loop through each cell in the maze
    for i in range(n):
        for j in range(m):
            # Base conditions:
            # If we encounter an obstacle or we are out of bounds, set dp[i][j] to 0.
            if i > 0 and j > 0 and maze[i][j] == -1:
                dp[i][j] = 0
                continue
            # If we are at the starting point, set dp[i][j] to 1.
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            
            # Initialize variables to store the number of paths coming from up and left.
            up = 0
            left = 0
            
            # If we can move up (i > 0), update 'up' with the value from the cell above.
            if i > 0:
                up = dp[i - 1][j]
            
            # If we can move left (j > 0), update 'left' with the value from the cell to the left.
            if j > 0:
                left = dp[i][j - 1]
            
            # Calculate the total number of paths to reach this cell and store it in dp[i][j].
            dp[i][j] = up + left
    
    # The result is stored in the bottom-right corner of the DP table.
    return dp[n - 1][m - 1]

def mazeObstacles(n, m, maze):
    # Create a DP table initialized with -1 values.
    dp = [[-1 for j in range(m)] for i in range(n)]
    
    # Call the utility function to find the number of paths.
    return mazeObstaclesUtil(n, m, maze, dp)

def main():
    # Example maze with 0s representing open paths and -1 representing obstacles.
    maze = [[0, 0, 0],
            [0, -1, 0],
            [0, 0, 0]]
    n = len(maze)
    m = len(maze[0])
    
    # Call the mazeObstacles function and print the result.
    print(mazeObstacles(n, m, maze))

a = [
    [0,0,0],
    [0,-1,0],
    [0,0,0]
]
m, n = 3, 3
dp = [[-1 for _ in range(n)] for _ in range(m)]
print("Ans:", f(m-1,n-1,a))
print("Ans:", f_memo(m-1,n-1,a, dp))
main()