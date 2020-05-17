import random

_values = ['rock', 'paper', 'scissors']
#          user         draw        win         loose
_game = [['rock',     ['rock',     'scissors', 'paper']],
         ['paper',    ['paper',    'rock',     'scissors']],
         ['scissors', ['scissors', 'paper',    'rock']]]

_usr = _values.index(input())
_rnd = random.randint(0, 2)
_res = ["There is a draw ({})".format(_game[_usr][1][_rnd]),
        "Well done. Computer chose {} and failed".format(_game[_usr][1][_rnd]),
        "Sorry, but computer chose {}".format(_game[_usr][1][_rnd])]
print(_res[_rnd])
