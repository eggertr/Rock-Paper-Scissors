import random
import os
import sys

_values = ['rock', 'paper', 'scissors']
#          user         lose        draw        win
_game = [['rock',     ['paper',     'rock',      'scissors']],
         ['paper',    ['scissors',  'paper',     'rock']],
         ['scissors', ['rock',      'scissors',  'paper']]]

members = []


def get_score(_name):
    _lin = []
    _sc = 0

    file = open('rating.txt', 'r')
    for line in file:
        members.append(line.replace("\n", ""))
        # print(repr(members))
        _lin = line.split(" ")
        if _lin[0] == _name:
            _sc = _lin[1]

    file.close()
    return int(_sc)


def update_score():

    _lin = []
    with open('rating.txt', "w") as fp:
        for line in members:
            _lin = line.split(" ")
            if _lin[0] == _player:
                _lin1 = _score
            else:
                _lin1 = _lin[1]

            print(_lin[0], _lin1, sep=" ", end="\n", file=fp)

    fp.close()


_player = input("Enter your name:")
print("Hello, {}".format(_player))
_score = get_score(_player)
_act = ""

while not _act == "!exit":

    _act = input()

    if _act in _values:
        _usr = _values.index(_act)
        _rnd = random.randint(0, 2)

        _res = ["Sorry, but computer chose {}".format(_game[_usr][1][_rnd]),
                "There is a draw ({})".format(_game[_usr][1][_rnd]),
                "Well done. Computer chose {} and failed".format(_game[_usr][1][_rnd])
                ]
        print(_res[_rnd])
        _score = _score + 50 * _rnd  # _rnd:0 is lose, _rnd:1 is draw, _rnd:2 is win
    elif _act == "!rating":
        print("Your rating is {}".format(_score))
    elif _act == "!exit":
        update_score()
        print("Bye!")
        break
    else:
        print("Invalid input")

