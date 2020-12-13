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

    def AllowsMoveX(self, col):
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

    def AllowsMoveY(self, col):
        if col < 0 or col > self.width:
            return False
        if self.board[0][col] != ' ':
            return False
        return True

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
    print('Welcome to Connect Four!')
    view.__str__()
    while controller.WinsFor('x') is False and controller.WinsFor('o') is False:
        x = input('''X's choice:''')
        if model.AllowsMoveX(x) is True:
            model.AddMove(x, 'X')
        else:
            while model.AllowsMoveX(x) is False:
                print('The move is invalid')
                view.__str__()
                x = input('''X's choice:''')
                if model.AllowsMoveX(x) is True:
                    model.AddMove(x, 'X')
                    break
        if (controller.WinsFor('X')):
            print('X wins -- Congratulations!')
            view.__str__()
            break
        view.__str__()
        ai = random.randint(0, 1)
        if ai == 0:
            y = int(x)
        else:
            ai2 = random.randint(0, 1)
            if ai2 == 0:
                y = int(x) - 1
            else:
                y = int(x) + 1
        if model.AllowsMoveY(y) is True:
            model.AddMove(y, 'O')
        else:
            while model.AllowsMoveY(y) is False:
                if y > 6:
                    y -= random.randint(1, 2)
                elif y < 0:
                    y += random.randint(1, 2)
                else:
                    y = random.randint(0, 6)
                if model.AllowsMoveY(y) is True:
                    model.AddMove(y, 'O')
                    break
                
        if (controller.WinsFor('O')):
            print('O wins -- Congratulations!')
            view.__str__()
            break
        view.__str__()


HostGame()
