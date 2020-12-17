'''
These unit tests are run on a file seperate to the final connect 4
game containing only the Model class becuase of how pytest handles
inputs. In order to test the full connect 4 game, pytest's
monkeypatch feature is required and thus identical paths to the
file are needed. Testing this seperate file allows the avoidance
of file path's which makes these pytests runable on different
computers.
'''
import pytest
from model_test import Model

model = Model()


def test_allows_players1():
    '''
    Ensure the method allows_players does not return True for strings
    with a length longer than 1.
    '''
    assert model.allows_players('10') is False


def test_allows_players2():
    '''
    Ensure the method allows_players does not return True for non-digit
    values.
    '''
    assert model.allows_players('h') is False


def test_allows_players3():
    '''
    Ensure that the method allows_players returns True for acceptable
    values of players.
    '''
    assert model.allows_players('1')


def test_allows_player_move1():
    '''
    Ensure that the method allows_player_move returns False for
    non-digit values.
    '''
    assert model.allows_player_move('hello') is False


def test_allows_player_move2():
    '''
    Ensure that the method allows_player_move returns False for
    digit values outside of the range of the connect 4 board.
    '''
    assert model.allows_player_move('8') is False


def test_allows_player_move():
    '''
    Ensure that the method allows_player_move returns True for
    acceptable values of col.
    '''
    assert model.allows_player_move('4')


def test_allows_computer_move1():
    '''
    Ensure that the method allows_computer_move returns False for
    values outside of the range of the connect 4 board.
    '''
    assert model.allows_computer_move('7') is False


def test_allows_computer_move():
    '''
    Ensure that the method allows_computer_move returns True for
    acceptable values of col.
    '''
    assert model.allows_computer_move('2')
