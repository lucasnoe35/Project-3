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
    
    def allows_players(self, players):
        if len(players) > 1:
            return False
        if players.isdigit() is not True:
            return False
        if int(players) < 1 or int(players) > 2:
            return False
        return True

    def allows_player_move(self, col):
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

    def allows_computer_move(self, col):
        if int(col) < 0 or int(col) > 6:
            return False
        if self.board[0][int(col)] != ' ':
            return False
        return True

    def get_computer_move(self, col):
        ox = 'X'
        if self.allows_computer_move(col):
            computer_move = col
        else:
            computer_move = random.randint(0,6)
        for i in range(self.width - 1):
            for j in range(self.height - 1):
                if self.board[j][i] == ox and self.board[j + 1][i + 1] == ox:
                    if self.allows_computer_move(i - 1) and self.board[j - 1][i - 1] == ' ':
                        computer_move = (i - 1)
                    elif j < self.height - 2 and self.allows_computer_move(i + 2) and self.board[j + 2][i + 2] == ' ':
                        computer_move = (i + 2)
        for i in range(self.width - 1):
            for j in range(1, self.height):
                if self.board[j][i] == ox and self.board[j - 1][i + 1] == ox:
                    if j < self.height - 2 and self.allows_computer_move(i - 1) and self.board[j + 1][i - 1] == ' ':
                        computer_move = (i - 1)
                    elif self.allows_computer_move(i + 2) and self.board[j - 2][i + 2] == ' ':
                        computer_move = (i + 2)
        for i in range(self.width - 1):
            for j in range(self.height):
                if self.board[j][i] == ox and self.board[j][i + 1] == ox:
                    if self.allows_computer_move(i - 1) and self.board[j][i - 1] == ' ':
                        computer_move = (i - 1)
                    elif self.allows_computer_move(i + 2) and self.board[j][i + 2] == ' ':
                        computer_move = (i + 2)
        for i in range(self.width):
            for j in range(self.height - 1):
                if self.board[j][i] == ox and self.board[j + 1][i] == ox:
                    if self.allows_computer_move(i) and self.board[j - 1][i] == ' ':
                        computer_move = (i)
                    elif j < self.height - 2 and self.allows_computer_move(i) and self.board[j + 2][i] == ' ':
                        computer_move = (i)
        for i in range(self.width - 2):
            for j in range(self.height - 2):
                if self.board[j][i] == ox and self.board[j + 1][i + 1] == ox\
                   and self.board[j + 2][i + 2] == ox:
                    if self.allows_computer_move(i - 1) and self.board[j - 1][i - 1] == ' ':
                        computer_move = (i - 1)
                    elif j < self.height - 3 and self.allows_computer_move(i + 3) and self.board[j + 3][i + 3] == ' ':
                        computer_move = (i + 3)
        for i in range(self.width - 2):
            for j in range(2, self.height):
                if self.board[j][i] == ox and self.board[j - 1][i + 1] == ox\
                   and self.board[j - 2][i + 2] == ox:
                    if j < self.height - 3 and self.allows_computer_move(i - 1) and self.board[j + 1][i - 1] == ' ':
                        computer_move = (i - 1)
                    elif self.allows_computer_move(i + 3) and self.board[j - 3][i + 3] == ' ':
                        computer_move = (i + 3)
        for i in range(self.width - 2):
            for j in range(self.height):
                if self.board[j][i] == ox and self.board[j][i + 1] == ox and\
                   self.board[j][i + 2] == ox:
                    if self.allows_computer_move(i - 1) and self.board[j][i - 1] == ' ':
                        computer_move = (i - 1)
                    elif self.allows_computer_move(i + 3) and self.board[j][i + 3] == ' ':
                        computer_move = (i + 3)
        for i in range(self.width):
            for j in range(self.height - 2):
                if self.board[j][i] == ox and self.board[j + 1][i] == ox and\
                   self.board[j + 2][i] == ox:
                    if self.allows_computer_move(i) and self.board[j - 1][i] == ' ':
                        computer_move = (i)
                    elif j < self.height - 3 and self.allows_computer_move(i) and self.board[j + 3][i] == ' ':
                        computer_move = (i)
        return computer_move

    def add_move(self, col, ox):
        '''
        Add an ox checker, where ox is a variable holding a
        string that is either "X" or "O", into column col.
        '''
        for i in range(self.height - 1, -1, -1):
            if(self.board[i][int(col)] == ' '):
                self.board[i][int(col)] = ox
                break

    def set_board(self, MoveString):
        """
        Take in a string of columns and place alternating checkers
        in those columns, starting with 'X'. For example, call
        b.set_board('012345') to see 'X's and 'O's alternate on the
        bottom row, or b.set_board('000000') to see them alternate
        in the left column. MoveString must be a string of
        integers.
        """
        NextCh = 'X'  # start by playing 'X'
        for ColString in MoveString:
            col = int(ColString)
            if 0 <= col <= self.width:
                self.add_move(col, NextCh)
            if NextCh == 'X':
                NextCh = 'O'
            else:
                NextCh = 'X'

    def delete_move(self, col):
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

    def wins_for(self, ox):
        pass


class Controller(Model):
    def __init__(self, Model):
        self.board = Model.board
        self.width = Model.width
        self.height = Model.height

    def wins_for(self, ox):
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


def host_game():
    '''
    Runs a loop which allows the user to play a game.
    '''
    model = Model()
    view = View(model)
    controller = Controller(model)
    players = input('''Welcome to Connect Four!\nPress 1 for one player and 2 for two player.\n''')
    while model.allows_players(players) is False:
        players = input('Please enter 1 for one player or 2 for two players.\n')
    view.__str__()
    while controller.wins_for('x') is False and controller.wins_for('o') is False:
        x = input('''X's choice:''')
        if model.allows_player_move(x):
            model.add_move(x, 'X')
        else:
            while model.allows_player_move(x) is False:
                print('The move is invalid')
                view.__str__()
                x = input('''X's choice:''')
                if model.allows_player_move(x):
                    model.add_move(x, 'X')
                    break
        if (controller.wins_for('X')):
            view.__str__()
            print('X wins -- Congratulations!')
            break
        view.__str__()
        if players == '1':
            computer_move = model.get_computer_move(x)
            model.add_move(computer_move, 'O')
        if players == '2':
            y = input('''O's choice:''')
            if model.allows_player_move(y):
                model.add_move(y, 'O')
            else:
                while model.allows_player_move(y) is False:
                    print('The move is invalid')
                    view.__str__()
                    y = input('''O's choice:''')
                    if model.allows_player_move(y):
                        model.add_move(y, 'O')
                        break           
        if (controller.wins_for('O')):
            view.__str__()
            if players == '2':
                print('O wins -- Congratulations!')
            if players == '1':
                print('You lose-- Try Again')
            break
        view.__str__()


host_game()
