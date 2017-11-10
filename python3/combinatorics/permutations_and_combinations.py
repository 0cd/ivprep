#!env python3

'''
Write methods to get permutations and combinations of a subset of items
'''

def getCombinations(items, r, start = 0, thisC = None):
    if thisC == None: thisC = []

    if len(thisC) == r:
        yield thisC[:]
    else:
        for i in range(start, len(items)):
            thisC.append(items[i])
            for c in getCombinations(items, r, i + 1, thisC):
                yield c
            thisC.pop()
                
def getPermutations(items, r, used = None, thisP = None):
    if thisP == None: thisP = []
    if used == None: used = [False] * len(items)

    if len(thisP) == r:
        yield thisP[:]
    else:
        for i in range(0, len(items)):
            if used[i]: continue
            thisP.append(items[i])
            used[i] = True
            for p in getPermutations(items, r, used, thisP):
                yield p
            thisP.pop()
            used[i] = False

if __name__ == "__main__":
    print("Two-letter combinations from \"abcd\" -")
    for combination in getCombinations("abcd", 2):
        print(combination)

    print("")

    print("Two-letter permutations from \"abcd\" -")
    for combination in getPermutations("abcd", 2):
        print(combination)

''' Output
Two-letter combinations from "abcd" -
['a', 'b']
['a', 'c']
['a', 'd']
['b', 'c']
['b', 'd']
['c', 'd']

Two-letter permutations from "abcd" -
['a', 'b']
['a', 'c']
['a', 'd']
['b', 'a']
['b', 'c']
['b', 'd']
['c', 'a']
['c', 'b']
['c', 'd']
['d', 'a']
['d', 'b']
['d', 'c']
'''