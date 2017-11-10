#!env python3

'''
Write a method to return all subsets of a set
'''

from permutations_and_combinations import get_combinations

def get_subsets(s):
    l = list(s)
    for size in range(1, len(s)+1):
        for c in get_combinations(l, size):
            yield c

if __name__ == "__main__":
    for s in get_subsets("abc"):
        print(s)