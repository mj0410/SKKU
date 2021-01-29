class Node :
    def __init__(self, data, up=None, down=None, left=None, right=None) :
        self.data = data
        self.up = up
        self.down = down
        self.left = left
        self.right = right

maze = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
        [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
        [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
        [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
        [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
        [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]

for i in range(0, 9) :
    for j in range(0, 9):
        node = Node(maze[i][j])
        if i==0 :
            if j==0 :
                node.down = maze[i+1][j]
                node.right = maze[i][j+1]
            elif j==9 :
                node.down = maze[i+1][j]
                node.left = maze[i][j-1]
            else :
                node.down = maze[i+1][j]
                node.left = maze[i][j-1]
                node.right = maze[i][j+1]

        elif i==9 :
            if j==0 :
                node.up = maze[i-1][j]
                node.right = maze[i][j+1]
            elif j==9 :
                node.up = maze[i-1][j]
                node.left = maze[i][j-1]
            else :
                node.up = maze[i-1][j]
                node.left = maze[i][j-1]
                node.right = maze[i][j+1]

        else :
            if j==0 :
                node.up = maze[i-1][j]
                node.down = maze[i+1][j]
                node.right = maze[i][j+1]
            elif j==9 :
                node.up = maze[i-1][j]
                node.down = maze[i+1][j]
                node.left = maze[i][j-1]
            else :
                node.up = maze[i-1][j]
                node.down = maze[i+1][j]
                node.left = maze[i][j-1]
                node.right = maze[i][j+1]
