def coin_change_min(N, S):
    """
    Minimum amount of coins needed to make N
    """
    # dp[i] is minimum coins needed to make amount i
    dp = [0] * (N + 1)

    for curr_amt in range(1, N+1):
        min_val = float("inf")
        for coin_val in S:
            if curr_amt >= coin_val:
                num_ways = 1 + dp[curr_amt - coin_val]
                min_val = min(min_val, num_ways)

            dp[curr_amt] = min_val

    return dp[N]


if __name__ == "__main__":

    S = [1,7, 10]
    N = 14

    print(coin_change_min(N, S))

    S = [1, 5, 10, 25]
    N = 98

    print(coin_change_min(N, S))
