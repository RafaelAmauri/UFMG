import random
from time import time

def merge(firstHalf, secondHalf, bestBuy1, bestSell1, bestBuy2, bestSell2):
    bestProfit1 = bestSell2 - min(min(firstHalf), bestBuy2)
    bestProfit2 = max(max(secondHalf), bestSell1) - bestBuy1

    if bestProfit1 > bestProfit2:
        bestBuyOverall  = min(min(firstHalf), bestBuy2)
        bestSellOverall = bestSell2

    else:
        bestBuyOverall  = bestBuy1
        bestSellOverall = max(max(secondHalf), bestSell1)

    return firstHalf + secondHalf, bestBuyOverall, bestSellOverall


def divideAndConquer(prices):
    if len(prices) == 2:
        if prices[0] < prices[1]:
            bestBuy  = prices[0]
            bestSell = prices[1]
        else:
            bestBuy  = prices[0]
            bestSell = prices[0]
        
        return prices, bestBuy, bestSell

    if len(prices) == 1:
        return prices, prices[0], prices[0]

    midPoint   = len(prices) // 2
    firstHalf,  bestBuy1, bestSell1 = divideAndConquer(prices[ : midPoint])
    secondHalf, bestBuy2, bestSell2 = divideAndConquer(prices[ midPoint : ])

    return merge(firstHalf, secondHalf, bestBuy1, bestSell1, bestBuy2, bestSell2)


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

prices = [ random.randint(0, 100000) for _ in range(4000000)]


#now = time()
#bestPrices = bruteForce(prices)
#durationBruteForce = time() - now
#print(f"Brute Force        = took {round(durationBruteForce, 10)} s and found the following prices: {bestPrices}")

now = time()
bestPrices = divideAndConquer(prices)[ 1 : ]
durationDivideAndConquer = time() - now
print(f"Divide and Conquer = took {round(durationDivideAndConquer, 10)} s and found the following prices: {bestPrices}")