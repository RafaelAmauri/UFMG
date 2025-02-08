import random
from time import time

def bruteForce(rankings):
    nInversions = 0
    for i in range(len(rankings)):
        for j in range(i + 1, len(rankings)):
            if rankings[i] > 2 * rankings[j]:
                nInversions += 1
    
    return nInversions


def merge(firstHalf, secondHalf, nInversions):
    # Sort both halves
    firstHalf.sort()
    secondHalf.sort()

    # Initialize pointers for both halves
    pointerFirstHalf  = 0
    pointerSecondHalf = 0

    # Iterate through both halves to count the number of significant inversions
    while pointerFirstHalf < len(firstHalf) and pointerSecondHalf < len(secondHalf):
        # If an inversion is found
        if firstHalf[pointerFirstHalf] > 2 * secondHalf[pointerSecondHalf]:
            # Add the number of remaining elements in the first half to nInversions
            nInversions += len(firstHalf) - pointerFirstHalf
            # Move to the next element in the second half
            pointerSecondHalf += 1
        else:
            # Move to the next element in the first half
            pointerFirstHalf += 1

    # Return the merged array and the updated inversion count
    return firstHalf + secondHalf, nInversions


def divideAndConquer(rankings, nInversions):
    # If the array has only one element, return it as is
    if len(rankings) == 1:
        return rankings, nInversions
    # If the array has two elements, check for significant inversion
    if len(rankings) == 2:
        nInversions += 0 if rankings[0]/2 <= rankings[1] else 1

        return rankings, nInversions

    midPoint   = len(rankings) // 2
    # Recursively divide and conquer the left half
    firstHalf, nInversions  = divideAndConquer(rankings[ : midPoint],  nInversions)
    # Recursively divide and conquer the right half
    secondHalf, nInversions = divideAndConquer(rankings[ midPoint : ], nInversions)

    # Merge the two halves and return the result
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