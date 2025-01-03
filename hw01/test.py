def count_binary_strings(n):
    dp = [0] * (n + 1)
    dp[1] = 2
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(count_binary_strings(12)) 
