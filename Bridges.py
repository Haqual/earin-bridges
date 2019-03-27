class Grid:
    board = [[]]
    size = 0
    def __init__(self, board, size):
        self.board=board
        self.size=size
        for x in range(self.size):
            for y in range(self.size):
                board[x][y]='e'

    def addIsland(self,connectionNum, x, y):
        if self.board[x][y] =='e':
             self.board[x][y] = connectionNum
        else:
            raise Exception('This space is already occupied by some island or bridge')
        #TODO: Finish the whole class of Grid
        #TODO: Add more functions such as:
        #TODO: Add addRoad within checking if it is valid
        #TODO: Add validation test of the whole grid
        #TODO: Read the grid from the file
        #TODO: More to come