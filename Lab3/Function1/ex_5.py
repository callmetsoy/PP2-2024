from itertools import permutations
def generate_permutations(string):
    for perm in permutations(string):
        print(''.join(perm))
    
generate_permutations('abc')