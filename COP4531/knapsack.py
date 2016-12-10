
def knapsack01(W, w, val):
	dp = [[None] * (W + 1) for _ in range(len(w) + 1)]
	for col in range(W + 1):
		dp[0][col] = 0
	for row in range( len(w) + 1):
		dp[row][0] = 0

	for i in range(1, len(w) +1):
		for j in range(1, W+1):
			# if the current item can't fit in knapsack of weight W
			if j < w[i - 1]:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = max( val[i - 1] + dp[i - 1][j - w[i - 1]],
								dp[i-1][j] )
	return dp[len(w)][W]

if __name__ == "__main__":
    w = [1,3,4,5]
    v = [1,4,5,7]
    W = 7

    print(knapsack01(W, w, v))