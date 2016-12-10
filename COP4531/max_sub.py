# dp solution

def max_subarray_dp(A):

    # dp[i] represents the max-subarray sum ending at index i
    # dp[i] = max(dp[i-1] + A[i], A[i])

    if len(A) == 0:
        return None

    dp = [None] * len(A)
    dp[0] = A[0]

    for i in range(1, len(A)):
        dp[i] = max(dp[i - 1] + A[i], A[i])

    return dp[len(A) - 1]
