
# there are 8 monkeys in the input file, we're not going to parse the file, we
# copy/pste in in here and convert it to code...

from dataclasses import dataclass
from typing import Callable

@dataclass
class Monkey:
    items: list
    operation: Callable
    test: Callable
    true_monkey: int 
    false_monkey: int
    inspections: int

monkeys = []

monkeys.append(Monkey(
    items        = [85, 79, 63, 72],
    operation    = lambda old: old * 17,
    test         = lambda x: x % 2 == 0,
    true_monkey  = 2,
    false_monkey = 6,
    inspections  = 0,
))

monkeys.append(Monkey(
    items        = [53, 94, 65, 81, 93, 73, 57, 92],
    operation    = lambda old: old * old,
    test         = lambda x: x % 7 == 0,
    true_monkey  = 0,
    false_monkey = 2,
    inspections  = 0,
))

monkeys.append(Monkey(
    items        = [62, 63],
    operation    = lambda old: old + 7,
    test         = lambda x: x % 13 == 0,
    true_monkey  = 7,
    false_monkey = 6,
    inspections  = 0,
))

monkeys.append(Monkey(
    items        = [57, 92, 56],
    operation    = lambda old: old + 4,
    test         = lambda x: x % 5 == 0,
    true_monkey  = 4,
    false_monkey = 5,
    inspections  = 0,
))

monkeys.append(Monkey(
    items        = [67],
    operation    = lambda old: old + 5,
    test         = lambda x: x % 3 == 0,
    true_monkey  = 1,
    false_monkey = 5,
    inspections  = 0,
))

monkeys.append(Monkey(
    items        = [85, 56, 66, 72, 57, 99],
    operation    = lambda old: old + 6,
    test         = lambda x: x % 19 == 0,
    true_monkey  = 1,
    false_monkey = 0,
    inspections  = 0,
))

monkeys.append(Monkey(
    items        = [86, 65, 98, 97, 69],
    operation    = lambda old: old * 13,
    test         = lambda x: x % 11 == 0,
    true_monkey  = 3,
    false_monkey = 7,
    inspections  = 0,
))

monkeys.append(Monkey(
    items        = [87, 68, 92, 66, 91, 50, 68],
    operation    = lambda old: old + 2,
    test         = lambda x: x % 17 == 0,
    true_monkey  = 4,
    false_monkey = 3,
    inspections  = 0,
))

# oke, let's hope i typed all this correctly...

# let's go
for r in range(20):
    for m, monkey in enumerate(monkeys):
        while len(monkey.items):
        
            worry_level_item = monkey.items.pop()
            worry_level = monkey.operation(worry_level_item)
            worry_level = round(worry_level // 3)  # relax it a bit
            test        = monkey.test(worry_level)
            # throw it:
            monkeys[monkey.true_monkey if test else monkey.false_monkey].items.append(worry_level)
            # some admin
            monkey.inspections += 1
            # some debug console output
            print( str(r), str(m), str(worry_level_item), str(worry_level),
                   str(test), str(monkey.true_monkey if test else monkey.false_monkey),
                   str(monkey.inspections))   

# That caused, some trouble, i started out with a namedtuple, but had to change it
# to a dataclass because a tuple cannot be changed (oh oh oh oh....)
# Than i had to google how to add a lambda to a data class

# any find the AOC answer and submit it...
n_of_inspections = []
for monkey in monkeys:
    n_of_inspections.append(monkey.inspections)
n_of_inspections.sort()
print(n_of_inspections)
monkey_business = n_of_inspections[-1] * n_of_inspections[-2]
print(monkey_business)

# i submitted 124605, it was wrong, too high, hmm start debugging....
# (start with test data? check definitions?....)

# oke checked the example data, and discovered that i should change
#   worry_level = round(worry_level / 3)  # relax it a bit
# to
#   worry_level = round(worry_level // 3)  # relax it a bit
# 
# i submitted the new answer 118674, and it was correct...
# i'm still not shure:
#
#    In [7]: round (3 / 2)
#    Out[7]: 2
#    
#    In [8]: round (3 // 2)
#    Out[8]: 1
#
# Oke 'close reading' did it, from the problem definition:
#
#  'divided by three and rounded down to the nearest integer'
#
# up to part 2






