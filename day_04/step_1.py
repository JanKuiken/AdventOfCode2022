
from collections import namedtuple

elve_pair = namedtuple('range_pair', ['first', 'second'])
range_pair = namedtuple('range_pair', ['start', 'end'])

elve_pairs = []    
with open('input.txt') as f:
    raw_data = f.readlines()
    for line in raw_data:
        line = line.strip()
        line = line.replace('-', ',')
        s = line.split(',')
        i = list(map(int, s))
        elve_pairs.append(elve_pair(
            range_pair(i[0], i[1]),
            range_pair(i[2], i[3])))

def fits_in(p1, p2):
    return p2.start >= p1.start and p2.end <= p1.end
    
total = 0
for pair in elve_pairs:
    if (   fits_in(pair.first,  pair.second) 
        or fits_in(pair.second, pair.first )):
        total += 1 

print(total)

print('---- part 2 ----')

def overlap(p1, p2):
    return p2.start <= p1.end and p2.end >= p1.start

total = 0
for pair in elve_pairs:
    if overlap(pair.first,  pair.second):
        total += 1 

print(total)

