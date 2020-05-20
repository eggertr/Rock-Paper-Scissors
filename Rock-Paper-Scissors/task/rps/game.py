import random
import os
import sys

_values = ['rock', 'paper', 'scissors']
members = []


def get_score(_name):
    _lin = []
    _sc = 0

    file = open('rating.txt', 'r')
    for line in file:
        # print(repr(line))
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


def rotate(_item):
    # This function rotates items in global list to the left, until selected item is in the middle.
    _len = len(_values)
    _mid = _len // 2

    while _values.index(_item) != _mid:
        _tmp = _values[0]
        _values.remove(_tmp)
        _values.append(_tmp)


_player = input("Enter your name:")
print("Hello, {}".format(_player))
_score = get_score(_player)
_act = ""
_ready = False
while not _act == "!exit":

    _act = input()

    if _act in _values:

        rotate(_act)  # Put user act in middle
        _rnd = random.randint(0, len(_values) - 1)
        _usr = _values.index(_act)

        if _usr > _rnd:
            print("Well done. Computer chose {} and failed".format(_values[_rnd]))
            _score += 100
        elif _usr == _rnd:
            print("There is a draw ({})".format(_values[_usr]))
            _score += 50
        else:
            print("Sorry, but computer chose {}".format(_values[_rnd]))

    elif _act == "!rating":
        print("Your rating: {}".format(_score))
    elif _act == "!exit":
        update_score()
        print("Bye!")
        break
    else:
        if len(_act) > 0:
            if " " not in _act and _act.isprintable() and _act.count(",") > 1:
                _values.clear()     # remove default values (rock,scissors,paper) and add new list.
                _values = _act.split(",")
                if len(_values) % 2 > 0:    # check if odd number of items
                    _ready = True
                    print("Okay, let's start")
                    continue
        else:
            if not _ready:
                _ready = True
                print("Okay, let's start")
                continue

        print("Invalid input")
