
# globals
grid = [] # will be list of lists, will be filled with int's, later a numpy array
start_pos = None
end_pos = None

# read and interpret input file
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        grid.append([])
        row = grid[-1]
        for ch in line:
            row.append(ord(ch) - ord('a'))
            if ch == 'S':
                start_pos = (len(grid)-1, len(row)-1)
                grid[start_pos[0]][start_pos[1]] = 0
            if ch == 'E':
                end_pos = (len(grid)-1, len(row)-1)
                grid[end_pos[0]][end_pos[1]] = ord('z') - ord('a')

# bring in the big guns....
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from copy import deepcopy

# make grid a numpy array
grid = np.asarray(grid)


print('start ', str(start_pos))
print('end   ', str(end_pos))

n_rows, n_cols = grid.shape
print(n_rows, n_cols)

# determine possible neighbours
possible_neighbours = []
for row in range(n_rows):
    possible_neighbours.append([])
    for col in range(n_cols):
        possible_neighbours[-1].append(set())
possible_neighbours = np.asarray(possible_neighbours)

# some fun with functions....
# utility functions.... return None or new row,col
def up(row,col):
    if row > 0 : 
        return row-1,col
def down (row,col):
    if row < (n_rows-1):
        return row+1,col
def left (row,col):
    if col > 0:
        return row,col-1
def right(row,col):
    if col < (n_cols-1):
        return row,col+1
directions = [up,down,left,right]

for row,col,direction in product(range(n_rows), range(n_cols), directions):
    if direction(row,col):
        if grid[row,col] >= (grid[direction(row,col)] - 1):
            possible_neighbours[row,col].add(direction(row,col))

# so much for the fun, now the serious business...

# i cheated and watched: https://www.youtube.com/watch?v=xhe79JubaZI

from collections import deque
from sys import exit


def shortest_route(pos):

    que = deque()
    visited = set()

    que.append((0,pos))
    visited.add(pos)

    while que:
        distance, current = que.popleft()
        for neighbour in possible_neighbours[current]:
        
            if neighbour in visited:
                continue
            
            if neighbour == end_pos:
                return(distance + 1)
            
            visited.add(neighbour)
            que.append((distance + 1, neighbour))


print(shortest_route(start_pos))

answer = 999999
for pos in product(range(n_rows), range(n_cols)):
    if grid[pos] == 0 :
        l = shortest_route(pos)
        if l:
            answer = min(answer, shortest_route(pos))
print(answer)

