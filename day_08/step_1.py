
# read forest from input
with open('input.txt') as f:
    lines = f.readlines()
    lines = [l.removesuffix('\n') for l in lines]
 
# convert input to a list of lists of integers
forest = []
for line in lines:
    row = []
    for ch in line:
        row.append(int(ch))
    forest.append(row)

print('---- part 1 ----')

# some admin
n_rows = len(forest)
n_cols = len(forest[0])

def create_boolean_forest():
    return [[False for col in range(n_cols)] for row in range(n_rows)]

visible_from_east  = create_boolean_forest()
visible_from_north = create_boolean_forest()
visible_from_west  = create_boolean_forest()
visible_from_south = create_boolean_forest()
visible            = create_boolean_forest()

# oke, lets fill the boolean forests, start with 'visible_from_east'
for row in range(n_rows):
    max_height = -1
    for col in range(n_cols):
        if forest[row][col] > max_height:
            max_height = forest[row][col]
            visible_from_east[row][col] = True

# next... 'visible_from_west'
for row in range(n_rows):
    max_height = -1
    for col in range(n_cols-1,-1,-1):
        if forest[row][col] > max_height:
            max_height = forest[row][col]
            visible_from_west[row][col] = True

# next... 'visible_from_north'
for col in range(n_cols):
    max_height = -1
    for row in range(n_rows):
        if forest[row][col] > max_height:
            max_height = forest[row][col]
            visible_from_north[row][col] = True

# next... 'visible_from_south'
for col in range(n_cols):
    max_height = -1
    for row in range(n_rows-1,-1,-1):
        if forest[row][col] > max_height:
            max_height = forest[row][col]
            visible_from_south[row][col] = True

# oke now combine the directions
for row in range(n_rows):
    for col in range(n_cols):
        visible[row][col] =    visible_from_north[row][col] \
                            or visible_from_south[row][col] \
                            or visible_from_east[row][col]  \
                            or visible_from_west[row][col] 

# count the visible trees
n_visible = 0
for row in range(n_rows):
    for col in range(n_cols):
        if visible[row][col]:
            n_visible += 1
            
print('visible from the outside :', str(n_visible))

print('---- part 2 ----')

def distance_to_last_tree_that_can_been_seen(row, col, d_row, d_col):
    distance = 0
    own_height = forest[row][col]
    for step in range(1, max([n_rows, n_cols])):  
        t_row = row + d_row * step
        t_col = col + d_col * step
        if t_row < 0 or t_row >= n_rows or t_col < 0 or t_col >= n_cols:
            return distance
        distance += 1
        if forest[t_row][t_col] >= own_height:
            return distance

max_scenic_score = 0
for row in range(1, n_rows):
    for col in range(1, n_cols):
        scenic_score = \
              distance_to_last_tree_that_can_been_seen(row, col,  1,  0) \
            * distance_to_last_tree_that_can_been_seen(row, col, -1,  0) \
            * distance_to_last_tree_that_can_been_seen(row, col,  0,  1) \
            * distance_to_last_tree_that_can_been_seen(row, col,  0, -1)
        #print(row, col, scenic_score)
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
print('max_scenic_score : ', str(max_scenic_score))


# some visual checks
def print_forest():
    print('== forest ==')
    for row in forest:
        for tree in row:
            print(tree, end='')
        print()
# print_forest()

def print_boolean_forest(boolean_forest):
    print('== boolean forest ==')
    for row in boolean_forest:
        for visible in row:
            print('#' if visible else '.', end='')
        print()
# print_boolean_forest(visible)


