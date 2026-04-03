"""
139. Word Break
Solved
Medium
Topics
premium lock icon
Companies
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
# https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=top-interview-150

# dp[i] = s의 앞 i 글자가 wordDict의 단어들로 완벽하게 쪼개지는가
# 유형: 구간 분할 DP
# 핵심 아이디어:
# DP[i]를 boolean으로 저장
# DP[0]=True인 빈 문자열로 두어 맨 처음 쪼개기 True 처리(applepen으로 따지면 dp[0]과 s[0:5] 둘 다 True => DP[5]=True)
# j를 기준으로 분할하여 앞부분인 s[0:j]가 쪼개지는지(dp[j]==True:) 뒷부분인 s[j:i]가 쪼개지는지(s[j:i] in wordDict:) and로 확인

class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True

        return dp[n]
