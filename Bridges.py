import copy

class Grid:
    board = [[]]
    size = 0

    def __init__(self, board, size):
        self.board = board
        self.size = size
        # for x in range(self.size):
        #   for y in range(self.size):
        #       board[x][y]='e'

    def addIsland(self, connectionNum, x, y):
        if self.board[x][y] == 'e':
            self.board[x][y] = str(connectionNum)
        else:
            print('This space is already occupied by some island or bridge')

    def isRoad(self, x, y, horizontal):
        if (x < 0 or x >= self.size or y < 0 or y >= self.size):
            return 0
        if ((self.board[x][y] == '-' and horizontal == True) or (self.board[x][y] == '|') and horizontal == False):
            return 1
        elif ((self.board[x][y] == '=' and horizontal == True) or (self.board[x][y] == '║' and horizontal == False)):
            return 2
        else:
            return 0

    def numOfRoads(self, x, y):

        result = self.isRoad(x, y - 1, True) + self.isRoad(x, y + 1, True) + self.isRoad(x - 1, y, False) + self.isRoad(
            x + 1, y, False)
        if (self.board[x][y].isdigit() == True):
            return result
        else:
            print('In the selected coordinates there is no island.')
#Function adding road a between two selected islands. If validation is true, it checks whether these points are islands, counts its roads already connected and validate if it is possible
#to connect these two islands
        #addRoad(first coordinate of first island, second coordinate of first island, first coordinate of second island, second coordinate of second island, (True- to way road, False - one way), True
    def addRoad(self, x1, y1, x2, y2, twoWay, validation):
        if validation == True:
            try:
                connectionNum1 = int(self.board[x1][y1])
                connectionNum2 = int(self.board[x2][y2])

                possibleConnections1 = connectionNum1 - self.numOfRoads(x1, y1)
                possibleConnections2 = connectionNum2 - self.numOfRoads(x2, y2)
                if (twoWay == True):
                    if (possibleConnections1 >= 2 and possibleConnections2 >= 2):
                        if (x1 == x2):
                            a=y1 if y1<y2 else y2
                            b=y2 if y2>y1 else y1
                            for i in range(a+1, b):
                                self.board[x1][i] = '='
                            return True #returning true if the road was added
                        elif (y1 == y2):
                            a=x1 if x1<x2 else x2
                            b=x2 if x2>x1 else x1
                            for i in range(a+1, b):
                                self.board[i][y1] = '║'
                            return True # returning true if the road was added
                        else:
                            print('That islands are not at the same line')

                    else:
                        print('Cannot create two way road between these islands.')

                else:
                    if (possibleConnections1 >= 1 and possibleConnections2 >= 1):
                        if (x1 == x2):
                            a=y1 if y1<y2 else y2
                            b=y2 if y2>y1 else y1
                            for i in range(a+1, b):
                                self.board[x1][i] = '-'
                            return True  # returning true if the road was added
                        elif (y1 == y2):
                            a=x1 if x1<x2 else x2
                            b=x2 if x2>x1 else x1
                            for i in range(a+1, b):
                                self.board[i][y1] = '|'
                            return True  # returning true if the road was added
                        else:
                            print('This islands are not at the same line')


            except ValueError as error:
                print('Cannot create a road because in the selected coordinates there is no city. ')

            except IndexError:
                print('This values are out of grid.')

    def validateGrid(self):
        possibleR=0
        realR=0
        for x in range(self.size):
            for y in range(self.size):
                if(self.board[x][y].isdigit()==True):

                    possibleR=possibleR+int(self.board[x][y])
                    realR=realR+self.numOfRoads(x,y)
                    if((int(self.board[x][y])-self.numOfRoads(x,y))>0):
                        print('At coordinates ('+str(x) +','+str(y)+') are not enough roads.')
                    elif ((int(self.board[x][y])-self.numOfRoads(x,y))<0):
                        print('At coordinates ('+str(x) +','+str(y)+') are too roads.')
        if((possibleR-realR)==0):
            return 1
        else:
            return 0
    def print(self):
        for x in range(self.size):
            for y in range(self.size):
                print(self.board[x][y], end=' ')
            print()

    def findNextH(self, x, y):

        r = range(1, 8)

        for i in range(y + 1, self.size):
            if self.board[x][i] != 'e':
                x2 = i
                return x2
        return 80

    def findNextV(self, x, y):

        r = range(1, 8)
        for i in range(x + 1, self.size):
            if self.board[i][y] != 'e':
                x2 = i
                return x2
        return 80
    #addroads -> adds horizontal and vertical road to the island on deepcopy board (only right and down)
    #vert, horiz -> True if 2 roads, false if 1 road
    def addRoads(self, x, y, vert, horiz):
        if (self.addRoad(x,y,x,self.findNextH(x,y),horiz,True)):
            if (self.addRoad(x, y, self.findNextV(x, y), y, vert, True)):
                return True
        else:
            return False

    # neighbours -> returns the list of possible neighbours (boards with added roads) fo the island [x,y]
    # needs addroad to return true or false
    def neighbours(self, x, y):
        nlist = []
        n =abs(int(self.board[x][y]) - self.numOfRoads(x,y))
        #print(n)
        if n==0:
            boardnext = copy.deepcopy(self)
            nlist.append(boardnext)
            return nlist
        elif n==1:

            boardnext = copy.deepcopy(self)
            boardnext1 = copy.deepcopy(self)

            if(boardnext.addRoad(x,y,x,boardnext.findNextH(x,y),False,True)==True):
                print("Option 1\n")
                boardnext.addRoad(x, y, x, boardnext.findNextH(x, y), False, True)
                nlist.append(boardnext)
            if(boardnext1.addRoad(x,y,boardnext1.findNextV(x,y),y,False,True)==True):
                print("Option 2\n")
                boardnext1.addRoad(x, y, boardnext1.findNextV(x, y), y, False, True)
                nlist.append(boardnext1)
            return nlist
        elif n==2:
            boardnext = copy.deepcopy(self)
            boardnext1 = copy.deepcopy(self)
            boardnext2 = copy.deepcopy(self)
            if (boardnext.addRoads(x, y, False, False) == True):
                boardnext = copy.deepcopy(self)

                boardnext.addRoads(x, y, False, False)
                nlist.append(boardnext)
                print("Option 11\n")

            if (boardnext1.addRoad(x, y, x,boardnext1.findNextH(x,y), True, True) == True):
                boardnext1 = copy.deepcopy(self)
                print("Option 12\n")
                boardnext1.addRoad(x, y, x, boardnext.findNextH(x,y), True, True)
                nlist.append(boardnext1)
            if ( boardnext2.addRoad(x, y, boardnext1.findNextV(x, y), y, True, True) == True):
                boardnext2 = copy.deepcopy(self)
                print("Option 13\n")
                boardnext2.addRoad(x, y, boardnext1.findNextV(x, y), y, True, True)
                nlist.append(boardnext2)

            return nlist
        elif n==3:
            boardnext = copy.deepcopy(self)
            boardnext1 = copy.deepcopy(self)
            if (boardnext.addRoads(x, y, False, True) == True):
                boardnext = copy.deepcopy(self)
                print("Option 11\n")
                boardnext.addRoads(x, y, False, True)
                nlist.append(boardnext)

            if (boardnext1.addRoads(x, y, True, False) == True):
                boardnext1 = copy.deepcopy(self)
                print("Option 11\n")
                boardnext1.addRoads(x, y, True, False)
                nlist.append(boardnext1)
            return nlist
        elif n==4:
            boardnext = copy.deepcopy(self)
            if (boardnext.addRoads(x, y, True, True) == True):
                boardnext = copy.deepcopy(self)
                print("Option 11\n")
                boardnext.addRoads(x, y, True, True)
                nlist.append(boardnext)
            return nlist


board = [['e', '1', 'e', '2', 'e', '3', 'e', 'e', '2', 'e', '2'],
         ['1', 'e', '2', 'e', '3', 'e', '2', 'e', 'e', '1', 'e'],
         ['e', 'e', 'e', 'e', 'e', '2', 'e', '2', 'e', 'e', '3'],
         ['3', 'e', '7', 'e', '5', 'e', 'e', 'e', 'e', 'e', 'e'],
         ['e', 'e', 'e', 'e', 'e', 'e', '3', 'e', '4', 'e', '4'],
         ['e', 'e', 'e', 'e', 'e', '2', 'e', 'e', 'e', 'e', 'e'],
         ['3', 'e', '6', 'e', '5', 'e', 'e', 'e', 'e', 'e', 'e'],
         ['e', 'e', 'e', 'e', 'e', 'e', '5', 'e', '7', 'e', '5'],
         ['e', 'e', 'e', 'e', 'e', '1', 'e', 'e', 'e', 'e', 'e'],
         ['e', 'e', '3', 'e', '6', 'e', '5', 'e', '3', 'e', '3'],
         ['3', 'e', 'e', '3', 'e', '2', 'e', '2', 'e', '1', 'e']]

myboard = Grid(board, 11)


myboard.addRoad(1,4,3,4,True,True)
#myboard.addRoad(3,2,3,4,True,True)

myboard.print()

myboard1 = copy.deepcopy(myboard)
#myboard1.addRoad(3, 2, 3, 4, True, True)
#print(myboard.board[0][3])

#print(myboard.findNextV(0,3))
myboard1.addRoad(0,3,myboard1.findNextV(0,3),3,True,True)
#myboard1.addRoad(0,3,myboard1.findNextV(0,3),3,True,True)
myboard.print()
print('\n')
myboard1.print()
myboard2 = copy.deepcopy(myboard1)
print('\n')
print(myboard2.addRoad(4, 6, 4, myboard2.findNextH(4,6), False, True))
print('\n')
myboard2.addRoad(2, 5, 2, myboard2.findNextH(2,5), False, True)
print('\n')
#print(myboard2.numOfRoads(2,5))
print('\n')
myboard2.print()
myboard3 = copy.deepcopy(myboard)
print('\n')
print(myboard3.addRoads(0,8,False,False))
print('\n')
myboard3.print()

a = myboard.neighbours(2,7)
print('\n')
#print(myboard.board[0][1])
print(len(a))
print('\n')
a[1].print()

b = myboard.neighbours(0,1)
print('\n')
#print(myboard.board[0][1])
print(len(b))
print('\n')
b[0].print()
#print()
#print(myboard3.addRoad(0,0,0,1,False,False))
#print(myboard.addRoad(0,1,myboard.findNextV(0,1),1,False,True))
#print(myboard.findNextV(0,1))
#myboard.print()
#myboard.validateGrid()
# TODO: Finish the whole class of Grid
# TODO: Add more functions such as:
# DONE: Add addRoad within checking if it is valid
# DONE: Add validation test of the whole grid
# TODO: Read the grid from 0 file

