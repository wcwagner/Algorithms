#bad recursive solution, with many overlapping subproblems
def LCS_recursive(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return 0
    elif X[-1] == Y[-1]:
        return 1 + LCS_recursive(X[:-1], Y[:-1])
    else:
        return max(LCS_recursive(X[:-1], Y),
                   LCS_recursive(X, Y[:-1]))

#DP solution
def LCS(X,Y):
    dp = [[None] * (len(X) + 1) for _ in range(len(Y) + 1)]

    for row in range(len(Y) + 1):
        dp[row][0] = 0
    for col in range(len(X) + 1):
        dp[0][col] = 0
    """
    dp[i][j] represents the LCS(X[:i], Y[:j])
    """
    for i in range(1, len(Y) + 1):
        for j in range(1, len(X) + 1):
            if X[j - 1] == Y[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max( dp[i-1][j],
                                dp[i][j-1])
    return dp[len(Y)][len(X)]


if __name__ == "__main__":
    X = "AXY"
    Y = "BAY"
    print(LCS(X, Y))
    X = "HIEROGLYPHOLOGY"
    Y = "MICHAELANGELO"
    print(LCS(X, Y))
