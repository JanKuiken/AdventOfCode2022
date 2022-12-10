
with open('input.txt') as f:
    lines = f.readlines()
    lines = [l.removesuffix('\n') for l in lines]

x = 1
cycle = 0
x_during_cycle = {}

for line in lines:
    if line == 'noop':
        cycle += 1
        x_during_cycle[cycle] = x
    else:  # addx <val>
        _, val = line.split(' ')
        cycle += 1
        x_during_cycle[cycle] = x
        cycle += 1
        x_during_cycle[cycle] = x
        x += int(val)        

sum_signal_strengths = sum([c * x_during_cycle[c] for c in range(20, 220+1, 40)])

print(sum_signal_strengths)

print('---- part 2 ----')
print()

for row in range(6):
    for col in range(40):
        cycle = 1 + 40 * row + col
        sprite = [ x_during_cycle[cycle] -1,
                   x_during_cycle[cycle],
                   x_during_cycle[cycle] +1 ]
        print('o' if col in sprite else ' ', end='')
    print()

