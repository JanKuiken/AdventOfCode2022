
# A minimal Folder class.
class Folder:
    def __init__(self, parent = None):
        self.parent = parent
        self.folders = {}  # k,v will be name(str), folder(Folder)
        self.files = {}    # k,v will be name(str), size(int)
    def add_folder(self, name):
        if not name in self.folders.keys():
            self.folders[name] = Folder(self)
    def add_file(self, name, size):
        self.files[name] = size
    def size(self):
        total = 0
        # add file sizes
        for size in self.files.values():
            total += size
        # add sub folder sizes
        for folder in self.folders.values():
            total += folder.size()
        return total

# initialize global variables
root    = Folder()
current = root
    
with open('input.txt') as f:
    lines = f.readlines()

# interpret all the lines
for line in lines:
    line = line.strip() # remove trailing '\n'

    if line.startswith('$ cd '):
        target_dir = line.removeprefix('$ cd ')
        if target_dir == '/':
            current = root
        elif target_dir == '..':
            current = current.parent
        else:
            current = current.folders[target_dir]
    elif line.startswith('$ ls'):
        pass # nothing to do
    else:
        # interpret output of ls
        size_or_dir, name = line.split(' ')
        if size_or_dir == 'dir':
            current.add_folder(name)
        else:
            current.add_file(name, int(size_or_dir))

# oke, find the answer...
sum_size_of_dirs_at_most_size_100000 = 0

def moeilijk(folder):
    global sum_size_of_dirs_at_most_size_100000
    if folder.size() <= 100000:
        sum_size_of_dirs_at_most_size_100000 += folder.size()
    for f in folder.folders.values():
        moeilijk(f)    

moeilijk(root) # doe moeilijk...
print(sum_size_of_dirs_at_most_size_100000)


print('---- part 2 ----')

total_space = 70000000
required_space = 30000000
used_space = root.size()
print('total space    : ', str(total_space))
print('used space     : ', str(used_space))
print('required_space : ', str(required_space))

free_space = total_space - used_space
to_be_freeed = required_space - free_space

print('to be freeed   : ', str(to_be_freeed))

# oke, find the answer...
dir_sizes = []

def moeilijk_2(folder):
    global dir_sizes
    dir_sizes.append(folder.size())
    for f in folder.folders.values():
        moeilijk_2(f)    

moeilijk_2(root) # doe moeilijk_2...

dir_sizes.sort()

for s in dir_sizes:
    if s > to_be_freeed:
        print('answer         : ', str(s))
        break

