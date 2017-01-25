import turtle
PART_OF_PATH = 'O'
OBSTACLE = '+'
TRIED = '.'
DEAD_END = '-'
START_POINT = 'S'

class Maze:
    def __init__(self, mazeFile):
        self.startRow = None
        self.startCol = None
        self.mazeList = []
        self.t = turtle.Turtle()
        row = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == START_POINT:
                    self.startRow = row
                    self.startCol = col
                col += 1
            self.mazeList.append(rowList)
            row += 1
        self.rowsOfMaze = len(self.mazeList)
        self.colsOfMaze = len(self.mazeList[0])
        self.wn = turtle.Screen()
        self.xTransition = -(self.colsOfMaze/2) + 0.5
        self.yTransition = self.rowsOfMaze/2 - 0.5
        self.wn.setworldcoordinates(-self.colsOfMaze/2, -self.rowsOfMaze/2, self.colsOfMaze/2, self.rowsOfMaze/2)
        
    def drawMaze(self):
        rows = self.rowsOfMaze
        cols = self.colsOfMaze
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(rows):
            for x in range(cols):
                if self.mazeList[y][x] == OBSTACLE:
                    self.drawCenteredBox(x + self.xTransition, -y + self.yTransition)
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self, x, y, color = 'orange'):
        self.t.pencolor(color)
        self.t.fillcolor(color)
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.down()
        self.t.setheading(90)
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self, x, y):
        # x is column number of the maze list
        # y is the negative row number of the maze list
        self.t.up()
        self.t.goto(x + self.xTransition, -y + self.yTransition)

    def dropBreadCrumb(self, color):
        self.t.dot(10, color)

    def updatePosition(self, row, col, val = None):
        if val:
            self.mazeList[row][col] = val
        self.moveTurtle(col, row)

        if val == OBSTACLE or val == DEAD_END:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == PART_OF_PATH:
            color = 'green'
        else:
            color = None

        if color:
            self.dropBreadCrumb(color)

    def isExit(self, row, col):
        rows = self.rowsOfMaze
        cols = self.colsOfMaze
        return row == rows - 1 or row == 0 or col == cols - 1 or col == 0

    def __getitem__(self, index):
        return self.mazeList[index]

def searchFrom(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)

    if maze[startRow][startColumn] == OBSTACLE:
        return False

    if maze[startRow][startColumn] == TRIED:
        return False

    if maze[startRow][startColumn] == DEAD_END:
        return False

    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True

    maze.updatePosition(startRow, startColumn, TRIED)

    found = searchFrom(maze, startRow - 1, startColumn) or \
            searchFrom(maze, startRow + 1, startColumn) or \
            searchFrom(maze, startRow, startColumn - 1) or \
            searchFrom(maze, startRow, startColumn + 1)
    
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)

    return found

if __name__ == '__main__':
    myMaze = Maze(open('maze.txt', 'r'))
    myMaze.drawMaze()
    startRow = myMaze.startRow
    startCol = myMaze.startCol
    searchFrom(myMaze, startRow, startCol)

