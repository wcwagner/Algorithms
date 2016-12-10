
def greedy(N):
    return N / 12 + (N % 12) / 5 + (N % 12 % 5) / 1


def min_coins(N, coins):
    dp = [0] * (N + 1)

    for i in range(1, N+1):
        if i <= 14:
            dp[i] = greedy(i)
            continue
        dp[i] = min([(1 + dp[i - c]) for c in [c for c in coins if c <= i]])

    return dp[N]
