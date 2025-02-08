import random
from time import time


def bruteForce(prices):
    bestProfit = 0
    bestBuy  = -1
    bestSell = -1

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > bestProfit:
                bestProfit = prices[j] - prices[i]
                bestBuy  = prices[i]
                bestSell = prices[j]
    
    return bestBuy, bestSell



def dynamicProgramming(prices):
    cache  = [ (0, i) for i in range(len(prices)) ]

    for i in range(1, len(prices)):
        aux = prices[i] - prices[i-1] + cache[i-1][0]
        if aux > 0:
            cache[i] = (aux, cache[i-1][1])
        else:
            cache[i] = (0, prices[i])

    bestProfit =  0
    bestBuy    = -1
    bestSell   = -1
    for i in range(len(cache)):
        currentProfit, currentBuy = cache[i]
        if currentProfit > bestProfit:
            bestBuy    = currentBuy
            bestProfit = currentProfit
            bestSell   = prices[i]

    return bestProfit, bestBuy, bestSell



prices = [ random.randint(0, 100000) for _ in range(4000000)]


now = time()
bestPrices = bruteForce(prices)
durationBruteForce = time() - now
print(f"Brute Force         = took {round(durationBruteForce, 10)} s and found the following prices: {bestPrices}")


now = time()
bestPrices = tuple(dynamicProgramming(prices)[ 1 : ])
durationDynamicProgramming = time() - now
print(f"Dynamic Programming = took {round(durationDynamicProgramming, 10)} s and found the following prices: {bestPrices}")