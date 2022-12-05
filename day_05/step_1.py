
# import some useful stuff...

from collections import deque
from collections import namedtuple
Move = namedtuple('Move', ['n', 'src', 'dst'])
from copy import deepcopy

# parse input

with open('input.txt') as f:
    lines = f.readlines()

# step 1, determine number of stacks (n_stacks)
for i, line in enumerate(lines):
    if line == '\n':  # empty line
        prev_line = lines[i-1]
        parts = prev_line.split()
        n_stacks = int(parts[-1])
        break # we're done

# step 2, determine initial state (state)
state = [deque() for _ in range(n_stacks)]
for line in lines:
    if '[' in line: # a line with initial state info, 
        # We've already manually checked that n_state = 9, and the initial
        # state lines are n_state * 4 characters long. 
        # So we can check for a space at certain position for a 'non crate'.
        # We use the convention that top is de right side of a Python
        # deque and bottom is the left side of a Python deque
        for i in range(n_stacks):
            crate = line[i*4+1]
            if crate != ' ':
                state[i].appendleft(crate)
    else:
        break # we're done

# step 3, determine the moves:
moves = []
for line in lines:
    if line.startswith('move '):
        line = line.strip() # remove trailing '\n' 
        line = line.removeprefix('move ') 
        n_str, remainder = line.split(' from ')
        src_str, dst_str = remainder.split(' to ')
        # note: the '-1', because computer nerds start counting at 0
        moves.append(Move(int(n_str), int(src_str)-1, int(dst_str)-1))

# added for part2:
state_2 = deepcopy(state)


# oke, after parsing the fun starts
for move in moves:
    for _ in range(move.n):
        state[move.dst].append(state[move.src].pop())

# hmm, that was all, collect the results..
for stack in state:
    print(stack[-1], end='')
print('\n')

print('=== part 2 ===')

# for part 2 we will use a temporary stack to simulate moving more
# than one crate at one time
temp_stack = deque()
for move in moves:
    for _ in range(move.n):
        temp_stack.append(state_2[move.src].pop())
    for _ in range(move.n):
        state_2[move.dst].append(temp_stack.pop())

# hmm, that was all, collect the results..
for stack in state_2:
    print(stack[-1], end='')
print('\n')

