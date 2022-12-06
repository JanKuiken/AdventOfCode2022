
with open('input.txt') as f:
    data = f.read()
    
data = data.strip() # remove trailing '\n', don't know why...

for i in range(4, len(data)):
    four_chars = data[i-4:i]
    if len(set(four_chars)) == 4: 
        print(i)
        break

print('---- part 2 ----')

for i in range(14, len(data)):
    fourteen_chars = data[i-14:i]
    if len(set(fourteen_chars)) == 14: 
        print(i)
        break

