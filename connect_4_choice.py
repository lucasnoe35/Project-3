import random

class Model(object):
    def __init__(self, width=7, height=6):
        '''
        Create the board object.
        '''
        self.width = width
        self.height = height
        self.board = []
        for i in range(0, height):
            self.board.append([])
            for j in range(0, width):
                self.board[i].append(' ')
    
    def AllowsPlayers(self, players):
        if len(players) > 1:
            return False
        if players.isdigit() is not True:
            return False
        if int(players) < 1 or int(players) > 2:
            return False
        return True

    def AllowsPlayerMove(self, col):
        '''
        Return True if the calling board object can allow a move into column c.
        '''
        if len(col) > 1:
            return False
        if col.isdigit() is not True:
            return False
        if(int(col) < 0 or int(col) >= self.width):
            return False
        if self.board[0][int(col)] != ' ':
            return False
        return True

    def AllowsComputerMove(self, col):
        if int(col) < 0 or int(col) > 6:
            return False
        if self.board[0][int(col)] != ' ':
            return False
        return True

    def GetComputerMove(self, col):
        ai1 = random.randint(0, 1)
        if ai1 == 0:
            computer_move = int(col)
        else:
            ai2 = random.randint(0, 1)
            if ai2 == 0:
                computer_move = int(col) - 1
            else:
                computer_move = int(col) + 1
        while self.AllowsComputerMove(computer_move) is False:
            if computer_move > 6:
                computer_move -= random.randint(1, 2)
            elif computer_move < 0:
                computer_move += random.randint(1, 2)
            else:
                computer_move = random.randint(0, 6)
        return computer_move

    def AddMove(self, col, ox):
        '''
        Add an ox checker, where ox is a variable holding a
        string that is either "X" or "O", into column col.
        '''
        for i in range(self.height - 1, -1, -1):
            if(self.board[i][int(col)] == ' '):
                self.board[i][int(col)] = ox
                break

    def SetBoard(self, MoveString):
        """
        Take in a string of columns and place alternating checkers
        in those columns, starting with 'X'. For example, call
        b.SetBoard('012345') to see 'X's and 'O's alternate on the
        bottom row, or b.SetBoard('000000') to see them alternate
        in the left column. MoveString must be a string of
        integers.
        """
        NextCh = 'X'  # start by playing 'X'
        for ColString in MoveString:
            col = int(ColString)
            if 0 <= col <= self.width:
                self.AddMove(col, NextCh)
            if NextCh == 'X':
                NextCh = 'O'
            else:
                NextCh = 'X'

    def DelMove(self, col):
        '''
        Remove the top checker from the column col.
        '''
        for i in range(0, self.height):
            if self.board[i][col] != ' ':
                self.board[i][col] = ' '
                break


class ViewEmpty(Model):
    def __init__(self, Model):
        pass

    def __str__(self):
        pass


class View(Model):
    def __init__(self, Model):
        self.height = Model.height
        self.width = Model.width
        self.board = Model.board

    def __str__(self):
        '''
        Print the board object in a specific format
        '''
        for i in range(0, self.height):
            row = '|'
            for j in range(0, self.width):
                row += self.board[i][j] + '|'
            print(row)
        print('-' * len(row))
        num_list = ''
        for x in range(0, self.width):
            num_list += ' ' + str(x)
        print(num_list)


class ControllerEmpty(Model):
    def __init__(self, Model):
        pass

    def WinsFor(self, ox):
        pass


class Controller(Model):
    def __init__(self, Model):
        self.board = Model.board
        self.width = Model.width
        self.height = Model.height

    def WinsFor(self, ox):
        '''
        Return True if a player won.
        '''
        for i in range(self.width - 3):
            for j in range(self.height):
                if self.board[j][i] == ox and self.board[j][i + 1] == ox and\
                   self.board[j][i + 2] == ox and self.board[j][i + 3] == ox:
                    return True
        for i in range(self.width):
            for j in range(self.height - 3):
                if self.board[j][i] == ox and self.board[j + 1][i] == ox and\
                   self.board[j + 2][i] == ox and self.board[j + 3][i] == ox:
                    return True
        for i in range(self.width - 3):
            for j in range(self.height - 3):
                if self.board[j][i] == ox and self.board[j + 1][i + 1] == ox\
                   and self.board[j + 2][i + 2] == ox and\
                   self.board[j + 3][i + 3] == ox:
                    return True
        for i in range(self.width - 3):
            for j in range(3, self.height):
                if self.board[j][i] == ox and self.board[j - 1][i + 1] == ox\
                   and self.board[j - 2][i + 2] == ox and\
                   self.board[j - 3][i + 3] == ox:
                    return True
        return False


def HostGame():
    '''
    Runs a loop which allows the user to play a game.
    '''
    model = Model()
    view = View(model)
    controller = Controller(model)
    players = input('''Welcome to Connect Four!\nPress 1 for one player and 2 for two player.\n''')
    while model.AllowsPlayers(players) is False:
        players = input('Please enter 1 for one player or 2 for two players.\n')
    view.__str__()
    while controller.WinsFor('x') is False and controller.WinsFor('o') is False:
        x = input('''X's choice:''')
        if model.AllowsPlayerMove(x) is True:
            model.AddMove(x, 'X')
        else:
            while model.AllowsPlayerMove(x) is False:
                print('The move is invalid')
                view.__str__()
                x = input('''X's choice:''')
                if model.AllowsPlayerMove(x) is True:
                    model.AddMove(x, 'X')
                    break
        if (controller.WinsFor('X')):
            view.__str__()
            print('X wins -- Congratulations!')
            break
        view.__str__()
        if players == '1':
            computer_move = model.GetComputerMove(x)
            model.AddMove(computer_move, 'O')
        if players == '2':
            y = input('''O's choice:''')
            if model.AllowsPlayerMove(y) is True:
                model.AddMove(y, 'O')
            else:
                while model.AllowsPlayerMove(y) is False:
                    print('The move is invalid')
                    view.__str__()
                    y = input('''O's choice:''')
                    if model.AllowsPlayerMove(y) is True:
                        model.AddMove(y, 'O')
                        break           
        if (controller.WinsFor('O')):
            view.__str__()
            print('O wins -- Congratulations!')
            break
        view.__str__()


HostGame()
