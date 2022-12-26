
# we need to exit abruptly... and copy stuff
from sys import exit
from copy import deepcopy

# our data structures (global vars)
rock = set()
sand = set()
rock_or_sand = set()
sand_source = (500,0)
abyss = None

#filename = "test_input.txt"
filename = "input.txt"

with open(filename) as f:
    for line in f:
        line = line.strip()
        points = line.split(" -> ")
        p0 = points[0]
        for p1 in points[1:]:
            x0, y0 = p0.split(",")
            x1, y1 = p1.split(",")
            x0 = int(x0)
            y0 = int(y0)
            x1 = int(x1)
            y1 = int(y1)
            if x0 == x1:
                for r in range(min(y0, y1), max(y0, y1) + 1):
                    rock.add((x0,r))
            elif y0 == y1:
                for r in  range(min(x0, x1), max(x0, x1) + 1):
                    rock.add((r,y0))
            else:
                raise ValueError("no line")
            
            p0 = p1
    rock_or_sand = deepcopy(rock)

def print_map():
    global abyss
    # yucky init of min/max with source point with some spacing
    min_x = 499
    max_x = 501
    min_y = -1
    max_y = +1
    for e in rock:
        min_x = min(min_x, e[0]-1)
        min_y = min(min_y, e[1]-1)
        max_x = max(max_x, e[0]+1)
        max_y = max(max_y, e[1]+1)
    # loop
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            c = "."
            if (x,y) in rock:
                c = "#"  
            if (x,y) in sand:
                c = "o"  
            if (x,y) == sand_source:
                c = "+"
            print(c, end="")
        print("")
    print("")
    abyss = max_y

print_map() # display stuff and set global 'abyss'

def next_position(position):
    x,y = position
    if not (x,y+1) in rock_or_sand:           # normal fall
        return (x,y+1)
    if not (x-1,y+1) in rock_or_sand:         # fall to the left
        return (x-1,y+1)
    if not (x+1,y+1) in rock_or_sand:         # fall to the right
        return (x+1,y+1)
    return position                           # else return input position

def sand_route():
    position = sand_source
    while True:
        new_position = next_position(position)
        x,y = new_position
        if new_position == position:
            # endpoint
            rock_or_sand.add(new_position)
            sand.add(new_position)
            break
        if y >= abyss:
            print("\n\nreached the abyss....\n\n")
            print_map()
            print("Number of sand units : ", str(len(sand)))
            # we're done
            exit(0)
        # continue...
        position = new_position

while True:
    sand_route()







