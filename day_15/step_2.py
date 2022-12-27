
from collections import namedtuple

Sensor = namedtuple("Sensor", ["s_x", "s_y", "b_x", "b_y"])

filename = "test_input.txt"
limit = 20
filename = "input.txt"
limit = 4000000

# data structures, global variables
sensors = []

with open(filename) as f:
    for line in f:
        line = line.removeprefix("\n")
        line = line.removeprefix("Sensor at x=")
        int_str, line = line.split(", y=", maxsplit=1)
        s_x = int(int_str)
        int_str, line = line.split(": closest beacon is at x=")
        s_y = int(int_str)
        int_str, line = line.split(", y=", maxsplit=1)
        b_x = int(int_str)        
        b_y = int(line)
        sensors.append(Sensor(s_x, s_y, b_x, b_y))

def manhattan_distance(sensor):
    return abs(sensor.s_x - sensor.b_x) + abs(sensor.s_y - sensor.b_y)

def range_at_some_y(sensor, y):
    y_dist_to_target = abs(y - sensor.s_y)
    spare_dist = manhattan_distance(sensor) - y_dist_to_target
    if spare_dist >= 0:
        return [sensor.s_x - spare_dist, sensor.s_x + spare_dist]  
    else:
        return []

def reduced_range(r1, r2):
    if r2[0] > (r1[1]+1) or r1[0] > (r2[1]+1):
        return []  # no overlapping/touching ranges
    else:
        return [min((r1[0], r2[0])), max((r1[1], r2[1]))]

ranges_at_target = None

def ranges_at_some_y(y):
    global ranges_at_target
    ranges_at_target = []
    
    for s in sensors:
        r = range_at_some_y(s,y)
        if r:
            ranges_at_target.append(r)

    #print(ranges_at_target)
    
    # complex recursive method to reduce ranges at target
    def reduce_ranges():
        global ranges_at_target
        for i1, r1 in enumerate(ranges_at_target):
            for i2, r2 in enumerate(ranges_at_target):
                if i1 != i2:
                    reducal = reduced_range(r1, r2)
                    if reducal:
                        ranges_at_target.remove(r1)
                        ranges_at_target.remove(r2)
                        ranges_at_target.append(reducal)
                        return False
        return True

    while True:
        if reduce_ranges():
            break

    #print(ranges_at_target)

    return ranges_at_target


for y in range(limit+1):
    dus = ranges_at_some_y(y)
    if len(dus) > 1:
        print(dus,y)
    
# results in :
# [[3138882, 4497514], [-1184066, 3138880]] 3364986

# manualy calculated the answer
answer = (3138880+1) * 4000000 + 3364986
print(answer)

