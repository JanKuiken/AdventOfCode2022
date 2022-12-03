
with open('input.txt') as f:
    rucksacks = f.readlines()

def priority(ch):
    if ch >= 'a' and ch <= 'z':
        return 1 + ord(ch) - ord('a')
    if ch >= 'A' and ch <= 'Z':
        return 27 + ord(ch) - ord('A')

total = 0
for r in rucksacks:
    r = r.strip()
    n = int(len(r)/2)
    comp_1 = set(r[:n])
    #print(r, str(n))
    comp_2 = set(r[n:])
    both = comp_1.intersection(comp_2)
    total += priority(both.pop())  # asumes 1 item in both

print(total)

print('---- part 2 ----')

total = 0
for i in range(0,len(rucksacks),3):
    s1 = set(rucksacks[i+0].strip())
    s2 = set(rucksacks[i+1].strip())
    s3 = set(rucksacks[i+2].strip())
    batch = s1.intersection(s2).intersection(s3)
    total += priority(batch.pop())  # asumes 1 item in both

print(total)

