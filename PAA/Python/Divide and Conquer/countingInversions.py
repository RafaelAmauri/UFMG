import random
from time import time

def bruteForce(rankings):
    nInversions = 0
    for i in range(len(rankings)):
        for j in range(i + 1, len(rankings)):
            if rankings[i] > rankings[j]:
                nInversions += 1
    
    return nInversions


def merge(firstHalf, secondHalf, nInversions):
    firstHalf.sort()
    secondHalf.sort()

    pointerFirstHalf  = 0
    pointerSecondHalf = 0

    while pointerFirstHalf < len(firstHalf) and pointerSecondHalf < len(secondHalf):
        if firstHalf[pointerFirstHalf] > secondHalf[pointerSecondHalf]:
            nInversions += len(firstHalf) - pointerFirstHalf
            pointerSecondHalf += 1
        else:
            pointerFirstHalf += 1

    return firstHalf + secondHalf, nInversions


def divideAndConquer(rankings, nInversions):
    if len(rankings) == 1:
        return rankings, nInversions
    if len(rankings) == 2:
        nInversions += 0 if rankings[0] <= rankings[1] else 1

        return rankings, nInversions

    midPoint   = len(rankings) // 2
    firstHalf, nInversions  = divideAndConquer(rankings[ : midPoint],  nInversions)
    secondHalf, nInversions = divideAndConquer(rankings[ midPoint : ], nInversions)

    return merge(firstHalf, secondHalf, nInversions)


quantNums = 20000 
rankings  = [ random.randint(0, quantNums) for i in range(0, quantNums) ]

now = time()
nInversions = bruteForce(rankings)
durationBruteForce = time() - now
print(f"Brute Force        = took {round(durationBruteForce, 10)} s and counted {nInversions} inversions")

now = time()
nInversions = divideAndConquer(rankings, 0)[1]
durationDivideAndConquer = time() - now
print(f"Divide and Conquer = took {round(durationDivideAndConquer, 10)} s and counted {nInversions} inversions")