
from collections import namedtuple

Sensor = namedtuple("Sensor", ["s_x", "s_y", "b_x", "b_y"])

#filename = "test_input.txt"
#target_y = 10
filename = "input.txt"
target_y = 2000000

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

def range_at_target_y(sensor):
    y_dist_to_target = abs(target_y - sensor.s_y)
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

ranges_at_target = []
for s in sensors:
    r = range_at_target_y(s)
    if r:
        ranges_at_target.append(r)

print("ranges at target", ranges_at_target)

# complex recursive method to reduce ranges at target
def reduce_ranges():
    for i1, r1 in enumerate(ranges_at_target):
        for i2, r2 in enumerate(ranges_at_target):
            if i1 != i2:
                reducal = reduced_range(r1, r2)
                if reducal:
                    ranges_at_target.remove(r1)
                    ranges_at_target.remove(r2)
                    ranges_at_target.append(reducal)
                    return True
    return False

while reduce_ranges():
    reduce_ranges()

print("ranges at target", ranges_at_target)

# manually checked that this reduced to only one range
remaining = ranges_at_target[0]

# but how many beacons are in this range....
beacons_in_this_range = set()
for s in sensors:
    if s.b_y == target_y:
        print(s.b_x)
        if s.b_x >= remaining[0] and s.b_x <= remaining[1]:
            beacons_in_this_range.add(s.b_x)

print("beacons_in_this_range : ", beacons_in_this_range)

answer = remaining[1] - remaining[0] + 1 - len(beacons_in_this_range)

print("answer : ", answer)





