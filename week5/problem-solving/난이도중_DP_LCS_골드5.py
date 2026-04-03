# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

"""
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

예제 입력 1 
ACAYKP
CAPCAK

예제 출력 1 
4
"""
X = input()
Y = input()
m = len(X)
n = len(Y)
LCS_table = [[0] * (n+1) for _ in range(m+1)]

# i, j = 0    
# if i or j == 0: LCS_table[i][j] = 0
# if m or n == 0: 
#     result = 0

# for i, j in X, Y:
#     if X[i] == Y[j]:
#         LCS_table[i][j] = LCS_table[i-1][j-1] + 1
#     elif X[i] != Y[j]:
#         LCS_table[i][j] = max(LCS_table[i-1][j], LCS_table[i][j-1])

# result = LCS_table[i][j]    
# print(result)

#------------------------------------------------------------------#

X = input()
Y = input()
m = len(X)
n = len(Y)
# 빈 문자열인 경우를 표현하기 위해 (0행과 열을 표현하기 위해) +1씩
LCS_table = [[0] * (n+1) for _ in range(m+1)]
   
# if m or n == 0: 
#     result = 0

for i in range(1, m+1):
    for j in range(1, n+1):
        if X[i-1] == Y[j-1]:
            LCS_table[i][j] = LCS_table[i-1][j-1] + 1
        elif X[i-1] != Y[j-1]:
            LCS_table[i][j] = max(LCS_table[i-1][j], LCS_table[i][j-1])

result = LCS_table[m][n]    
print(result)