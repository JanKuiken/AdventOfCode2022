
# there are 8 monkeys in the input file, we're not going to parse the file, we
# copy/paste it in here and convert it to code...

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

# let's go again
for _ in range(10000): # the monkeys will play 10000 rounds...
    for monkey in monkeys:
        while monkey.items:
        
            worry_level_item = monkey.items.pop()
            worry_level = monkey.operation(worry_level_item)  # increase it...
            #worry_level = round(worry_level // 3)             # relax it a bit
            
            # for part 2 we need a new worry level reduction function....
            # each test is: worry_level % <prime_number> .....
            # test(worry_level +/- n * (2*3*5*7*11*13*17*19)) will yield the 
            # same results as test(worry_level)
            product_of_used_primes = 2*3*5*7*11*13*17*19
            worry_level %= product_of_used_primes
            
            test        = monkey.test(worry_level)
            # throw item to another monkey:
            monkeys[monkey.true_monkey if test else monkey.false_monkey].items.append(worry_level)
            # some admin
            monkey.inspections += 1

# aquire desired answer
n_of_inspections = [monkey.inspections for monkey in monkeys]
n_of_inspections.sort()
monkey_business = n_of_inspections[-1] * n_of_inspections[-2]

print('---- part 2 ----')
print(monkey_business)

