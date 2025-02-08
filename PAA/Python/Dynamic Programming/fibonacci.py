num = 40
dp  = [0, 1]
def dynamicProgramming(n):
    if n == 0:
        return 0
    
    if len(dp) <= (n-1):
        dp.append(dynamicProgramming(n-1))

    return dp[n-1] + dp[n-2]

print(dynamicProgramming(num))

def recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return recursive(n-2) + recursive(n-1)

print(recursive(num))