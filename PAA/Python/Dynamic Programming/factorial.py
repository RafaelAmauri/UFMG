import time
import sys

sys.setrecursionlimit(10000)
nLoops = 9999

dp = [1]
def dynamicProgramming(n):
    if n == 0:
        return 1

    if len(dp) <= (n-1):
        dp.append(dynamicProgramming(n-1))

    return dp[n-1] * n


def recursive(n):
    if n == 0:
        return 1

    return recursive(n-1) * n


now = time.time()
for i in range(nLoops):
    dynamicProgramming(i)
timeDp = time.time() - now
print(f"Dynamic Programming = {round(timeDp, 10)} s")


now = time.time()
for i in range(nLoops):
    recursive(i)
timeRec = time.time() - now
print(f"Recursive           = {round(timeRec, 10)} s", end="\n\n")

print(f"Recursive was {round(timeRec/timeDp, 2)} times slower")