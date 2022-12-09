
from collections import namedtuple
from copy import copy, deepcopy
import matplotlib.pyplot as plt

Move = namedtuple('Move', ['dir', 'n'])
Pos = namedtuple('Pos', ['x', 'y'])

# global variables
head_pos = Pos(0,0)
tail_pos = Pos(0,0)
tail_visits = {Pos(0,0) : 1}  # count starting points as a visit
moves = []

# read input file, store moves
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line.removesuffix('\n')
        direction, number = line.split(' ')
        moves.append(Move(direction, int(number)))

def next_pos(pos, direction):
    if direction == 'U': return Pos(pos.x,pos.y+1)
    if direction == 'D': return Pos(pos.x,pos.y-1)
    if direction == 'L': return Pos(pos.x-1,pos.y)
    if direction == 'R': return Pos(pos.x+1,pos.y)
    raise ValueError('unknown direction')

def adjecent(pos1, pos2):
    dx = abs(pos1.x - pos2.x)
    dy = abs(pos1.y - pos2.y)
    return dx <= 1 and dy <= 1

def add_tail_visit(pos):
    global tail_visits
    if pos in tail_visits.keys(): 
        tail_visits[pos] += 1
    else:
        tail_visits[pos] = 1  

# oke, let's move
for move in moves:
    for _ in range(move.n):
        new_head_pos = next_pos(head_pos, move.dir)
        if not adjecent(new_head_pos, tail_pos):
            tail_pos = head_pos
            add_tail_visit(tail_pos)
        head_pos = new_head_pos

print('number of tail positions : ', str(len(tail_visits)))

