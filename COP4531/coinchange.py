
def change_recursive(N, S):
    if N == 0:
        return 1
    if N < 0 or len(S) == 0:
        return 0
    return change_recursive(N, S[:-1]) + change_recursive(N - S[-1], S)

def change(N, S):

    dp = [ [None] * (N + 1) for _ in range(len(S) + 1)]
    # initial conditions
    for row in range(len(S) + 1):
        dp[row][0] = 1
    for col in range(N + 1):
        dp[0][col] = 0

    for i in range(1, len(S) + 1):
        for j in range(1, N + 1):
            if j - S[i - 1] >= 0:
                dp[i][j] = dp[i][j - S[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(S)][N]
if __name__ == "__main__":
    print(change(4, [1,2,3]))
    print(change(5, [1,2,3]))

