#!env python3

'''
Given an infinite supply of quarters dimes nickels and coppers generate
all possible combinations of denominations totalling to a given sum S.
'''

def getCoinCombinations(total, coins = (1, 5, 10, 25), start = 0, combination = None):
    if combination == None: combination = []
    if total == 0:
        yield combination[:]
    else:
        for i in range(start, len(coins)):
            coin = coins[i]
            remaining = total - coin
            if remaining < 0: break
            combination.append(coin)
            for c in getCoinCombinations(remaining, coins, i, combination):
                yield c
            combination.pop()

if __name__ == "__main__":
    for combination in getCoinCombinations(12):
        print(combination)

'''Output
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 5]
[1, 1, 5, 5]
[1, 1, 10]
'''