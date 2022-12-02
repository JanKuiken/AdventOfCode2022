
with open('input.txt') as f:
    data = f.read()
    data = data[:-1] # strip last \n

elves = data.split('\n\n')

elves_calories = []
for elve in elves:
    calories = elve.split('\n')
    calories = map(int, calories)
    calories = sum(calories)
    elves_calories.append(calories)

elves_calories.sort()
print(elves_calories[-1])
print('---- part 2 ----')
print(sum(elves_calories[-3:]))

