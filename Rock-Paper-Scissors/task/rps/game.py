import random
import os
import sys

_values = ['rock', 'paper', 'scissors']
#          user         draw        win         loose
_game = [['rock',     ['rock',     'scissors', 'paper']],
         ['paper',    ['paper',    'rock',     'scissors']],
         ['scissors', ['scissors', 'paper',    'rock']]]


def get_score(_name):
    _lin = []
    file = open('rating.txt', 'r')
    for line in file:
        _lin = line.split(" ")
        if _lin[0] == _player:
            break
    file.close()
    if len(_lin[1]) > 0:
        return _lin[1]
    else:
        return 0


_player = input("Enter your name:")
print("Hello, {}".format(_player))
_score = get_score(_player)
exit()
_act = ""
while not _act == "exit":

    _act = input()

    if _act in _values:
        _usr = _values.index(_act)
        _rnd = random.randint(0, 2)
        _res = ["There is a draw ({})".format(_game[_usr][1][_rnd]),
                "Well done. Computer chose {} and failed".format(_game[_usr][1][_rnd]),
                "Sorry, but computer chose {}".format(_game[_usr][1][_rnd])]
        print(_res[_rnd])
    elif _act == "exit":
        print("Bye!")
        break
    else:
        print("Invalid input")