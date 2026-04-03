# 빈 배열 생성 버전(O(n^2))
class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)

        # 2D dp 초기화: 행 i는 길이 i+1
        dp = [[0] * (i + 1) for i in range(n)]

        # 베이스 케이스: 마지막 행 그대로 복사
        dp[n-1] = list(triangle[n-1])

        # 아래에서 위로
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])

        return dp[0][0]

# 최적화 버전(O(n))
n = len(triangle)
dp = list(triangle[-1])

for i in range(n-2, -1, -1):
    for j in range(len(triangle[i])):
        dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
return dp[0]