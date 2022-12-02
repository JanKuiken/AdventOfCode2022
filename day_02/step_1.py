"""
Deze gaan we oplossen met 'lookup' dictionaries

(bij tiepfoutjes krijgen we wel een key-error)
"""

POINTS = {
    'Rock'     : 1, 
    'Paper'    : 2, 
    'Scissors' : 3,    
}

OUTCOMES = { 
    # wins
    ('Scissors', 'Paper')    : 6,    # Scissors beats papers
    ('Paper',    'Rock')     : 6,    # Paper beats Rock
    ('Rock',     'Scissors') : 6,    # Rock beats Scissors
    # draws 
    ('Rock',     'Rock')     : 3,
    ('Paper',    'Paper')    : 3,
    ('Scissors', 'Scissors') : 3,
    # losses
    ('Paper',    'Scissors')  : 0,
    ('Rock',     'Paper')     : 0,
    ('Scissors', 'Rock')      : 0,
}

FILE_SYMBOLS = {
    'A' : 'Rock', 
    'B' : 'Paper', 
    'C' : 'Scissors',
    'X' : 'Rock', 
    'Y' : 'Paper', 
    'Z' : 'Scissors',
}


with open('input.txt') as f:
    games = f.readlines()
    
def my_score(game):
    his_choice = FILE_SYMBOLS[game[0]]   # 1e char van regel
    my_choice  = FILE_SYMBOLS[game[2]]   # 3e char van regel
    return POINTS[my_choice] + OUTCOMES[(my_choice, his_choice)]
    
my_scores = [my_score(game) for game in games]    
my_total_score = sum(my_scores)
print(my_total_score)


print('---- part 2 ----')

REQUIRED_OUTCOME = { 'X': 0, 'Y': 3, 'Z': 6}

def find_my_choice(his_choice, required_outcome):
    for my_choice in ['Paper', 'Rock', 'Scissors']:
        if OUTCOMES[(my_choice, his_choice)] == required_outcome:
            return my_choice
    raise ValueError('should not occur')

def my_score_part_2(game):
    his_choice = FILE_SYMBOLS[game[0]]   # 1e char van regel
    required_outcome = REQUIRED_OUTCOME[game[2]]   # 3e char van regel
    my_choice = find_my_choice(his_choice, required_outcome)
    return POINTS[my_choice] + OUTCOMES[(my_choice, his_choice)]

my_scores = [my_score_part_2(game) for game in games]    
my_total_score = sum(my_scores)
print(my_total_score)

