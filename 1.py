pairs = [[1,2],[7,8],[4,5]]
pairs.sort()
dp = [1] * len(pairs)
for j in range(len(pairs)):
    for i in range(j):
        print(pairs[i][1], pairs[j][0])
        if pairs[i][1] < pairs[j][0]:
            dp[j] = max(dp[j], dp[i] + 1)
print(max(dp))