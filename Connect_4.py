class Board(object):
    
    def __init__(self, width=7, height=6):
        'creates the board object'
        self.width = width
        self.height = height
        self.board = []
        for i in range(0,height):
            self.board.append([])
            for j in range(0,width):
                self.board[i].append(' ')
    
    def __str__(self):
        'prints the board object in a specific format'
        for i in range(0,self.height):
            row = '|'
            for j in range(0,self.width):
                row += self.board[i][j] + '|'
            print(row) 
        print('-' * len(row))
        num_list = ''
        for x in range(0,self.width): 
            num_list += ' ' + str(x) 
        print(num_list)
     
    def allowsMove(self,col):
        'This method should return True if the calling Board object can allow a move into column c'
        if(col < 0 or col >= self.width):
            return False
        if self.board[0][col] != ' ':
            return False
        return True
    
    def addMove(self, col, ox):
        'This method should add an ox checker, where ox is a variable holding a string that is either "X" or "O", into column col'    
        for i in range(self.height - 1,-1,-1):
            if(self.board[i][col] == ' '):
                self.board[i][col] = ox
                break   
            
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
    alternating checkers in those columns,
    starting with 'X'

     For example, call b.setBoard('012345')
     to see 'X's and 'O's alternate on the
     bottom row, or b.setBoard('000000') to
     see them alternate in the left column.
     moveString must be a string of integers
     """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'   
                
    def delMove(self, col):
        'Removes the top checker from the column col'
        for i in range(0, self.height):
            if self.board[i][col] != ' ':
                self.board[i][col] = ' '
                break
                
    def winsFor(self, ox):
        'Returns True if a player won'
        for i in range(self.width - 3):
            for j in range(self.height):
                if self.board[j][i] == ox and self.board[j][i+1] == ox and self.board[j][i+2] == ox and self.board[j][i+3] == ox:
                    return True
        for i in range(self.width):
            for j in range(self.height-3):
                if self.board[j][i] == ox and self.board[j+1][i] == ox and self.board[j+2][i] == ox and self.board[j+3][i] == ox:
                    return True
        for i in range(self.width-3):
            for j in range(self.height-3):
                if self.board[j][i] == ox and self.board[j+1][i+1] == ox and self.board[j+2][i+2] == ox and self.board[j+3][i+3] == ox:
                    return True
        for i in range(self.width-3):
            for j in range(3,self.height):
                if self.board[j][i] == ox and self.board[j-1][i+1] == ox and self.board[j-2][i+2] == ox and self.board[j-3][i+3] == ox:
                    return True
        return False
    
    def hostGame(self):
        'Runs a loop which allows the user to play a game'
        print('Welcome to Connect Four!')
        self.__str__()
        while self.winsFor('x') == False and self.winsFor('o') == False:
            x = int(input('''X's choice:'''))
            if self.allowsMove(x) == True:
                self.addMove(x,'X')
            else:
                while self.allowsMove(x) == False:                    
                    print('The move is invalid')
                    self.__str__()
                    x = int(input('''X's choice:'''))
                    if self.allowsMove(x) == True:
                        self.addMove(x,'X')
                        break
            if (self.winsFor('X')):
                print('X wins -- Congratulations!')
                self.__str__()
                break
            self.__str__()
            y = int(input('''O's choice:'''))
            if self.allowsMove(y) == True:
                self.addMove(y,'O')
            else:
                while self.allowsMove(y) == False:                    
                    print('The move is invalid')
                    self.__str__()
                    y = int(input('''O's choice:'''))
                    if self.allowsMove(y) == True:
                        self.addMove(y,'O')
                        break
            if (self.winsFor('O')):
                print('O wins -- Congratulations!')
                self.__str__()
                break       
            self.__str__()
            
b = Board() 
b.hostGame()
    